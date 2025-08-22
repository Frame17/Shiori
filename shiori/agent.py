import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from phoenix.otel import register
from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel

from shiori.mcp_servers import get_all_mcp_tools
from shiori.prompts import BLOG_POSTS_PROMPT, RESEARCH_PAPERS_PROMPT

tracer_provider = register(
    project_name="Shiori",
    endpoint="http://localhost:6006/v1/traces",
    auto_instrument=True,
    set_global_tracer_provider=False,
    verbose=False,
)

load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

trace_provider = TracerProvider()
trace_provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(trace_provider)
tracer = trace.get_tracer(__name__)

TIME_PERIOD_TO_QUERY = {
    "d": "published yesterday",
    "w": "published in the last 7 days",
    "m": "published in the last 30 days",
    None: "",
}


def setup_agent() -> CodeAgent:
    """
    Set up and configure the AI agent with necessary tools.

    Returns:
        CodeAgent: Configured agent with tools for research and search
    """

    model = InferenceClientModel()
    if os.environ.get("LITELLM_API_KEY"):
        model = LiteLLMModel(
            api_base=os.environ.get("LITELLM_API_BASE"),
            model_id=os.environ.get("MODEL_ID"),
            api_key=os.environ.get("LITELLM_API_KEY"),
        )

    return CodeAgent(tools=get_all_mcp_tools(), model=model, instructions="")


def fetch_research_papers(
    agent: CodeAgent, time_period: str = None, count: int = 5
) -> str:
    """
    Fetch recent machine learning research papers within a specific time period.

    Returns:
        str: Markdown formatted research paper summaries
    """
    with tracer.start_as_current_span("fetch_papers"):
        prompt = RESEARCH_PAPERS_PROMPT.format(
            count=count, time_period=TIME_PERIOD_TO_QUERY.get(time_period, "")
        )
        return agent.run(prompt)


def fetch_blog_posts(agent: CodeAgent, time_period: str = None) -> str:
    """
    Fetch recent blog posts from major AI companies.

    Returns:
        str: Markdown formatted blog post summaries
    """
    with tracer.start_as_current_span("fetch_blogs"):
        prompt = BLOG_POSTS_PROMPT.format(
            time_period=TIME_PERIOD_TO_QUERY.get(time_period, "")
        )
        return agent.run(prompt)


def save_markdown_summary(
    papers_md: str, blog_md: str, output_path: str = "summary.md"
) -> None:
    output_file = Path(output_path)

    logger.info("Saving markdown summary to %s", output_file)
    with open(output_file, "w", encoding="utf-8") as f:
        if papers_md:
            f.write("## Research Papers\n")
            f.write(papers_md + "\n\n")
        if blog_md:
            f.write("# Recent Blog Posts\n\n")
            f.write("## Company Blog Posts\n")
            f.write(blog_md + "\n")
