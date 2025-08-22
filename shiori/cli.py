#!/usr/bin/env python3

import argparse
import logging
import sys

from pyfiglet import figlet_format
from rich.console import Console
from rich.text import Text

from shiori.agent import (
    fetch_blog_posts,
    fetch_research_papers,
    save_markdown_summary,
    setup_agent,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def print_banner():
    console = Console()

    ascii_banner = figlet_format("  Shiori  ", font="banner3-D")
    console.print(Text(ascii_banner, style="bold magenta"))

    console.print(
        "❤️ ✨ Shiori welcomes you, Believer in Research ... ✨ ❤️", style="bold cyan"
    )


def setup_argument_parser():
    parser = argparse.ArgumentParser(
        description="Machine Learning Research and Blog Aggregator CLI"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    research_parser = subparsers.add_parser("research", help="Fetch research papers")
    research_parser.add_argument(
        "--time",
        choices=["d", "w", "m"],
        default="w",
        help="Time period for filtering research papers (default: 1 week)",
    )
    research_parser.add_argument(
        "--output",
        default="papers_summary.md",
        help="Output file path (default: papers_summary.md)",
    )

    blog_parser = subparsers.add_parser("blog", help="Fetch blog posts")
    blog_parser.add_argument(
        "--time",
        choices=["d", "w", "m"],
        default="w",
        help="Time period for filtering blog posts (default: 1 week)",
    )
    blog_parser.add_argument(
        "--output",
        default="blog_summary.md",
        help="Output file path (default: blog_summary.md)",
    )

    return parser


def handle_research_command(time_period, output_file):
    try:
        agent = setup_agent()
        papers_md = fetch_research_papers(agent, time_period)
        save_markdown_summary(papers_md, "", output_file)

        logger.info(
            "Successfully generated research papers summary for the last %s",
            time_period,
        )
        logger.info("Output saved to %s", output_file)
    except Exception as e:
        logger.error("Error occurred: %s", e, exc_info=True)
        sys.exit(1)


def handle_blogposts_command(time_period, output_file):
    try:
        agent = setup_agent()
        blog_md = fetch_blog_posts(agent, time_period)
        save_markdown_summary("", blog_md, output_file)

        logger.info(
            "Successfully generated blog posts summary for the last %s", time_period
        )
        logger.info("Output saved to %s", output_file)
    except Exception as e:
        logger.error("Error occurred: %s", e, exc_info=True)
        sys.exit(1)


def execute_command(args, parser):
    command_handlers = {
        "research": lambda: handle_research_command(args.time, args.output),
        "blog": lambda: handle_blogposts_command(args.time, args.output),
    }

    handler = command_handlers.get(args.command)
    if handler:
        handler()
    else:
        parser.print_help()
        sys.exit(1)


def main():
    print_banner()

    parser = setup_argument_parser()
    args = parser.parse_args()

    execute_command(args, parser)

if __name__ == "__main__":
    main()