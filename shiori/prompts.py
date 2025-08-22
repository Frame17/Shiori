"""
Prompts for Shiori to do her homework.
"""

RESEARCH_PAPERS_PROMPT = """
Find top {count} most recent machine learning research papers from LLM and Deep Learning categories {time_period}.
For each paper, output a markdown list with **Title (as link)**, **Problem**, **Approach**, and **Evaluation**.
"""

BLOG_POSTS_PROMPT = """
Search for recent blog posts from top AI companies, such as OpenAI, Anthropic, Google DeepMind, 
Meta, Mistral, DeepSeek, xAI, Alibaba, ByteDance and JetBrains {time_period}.
Summarize each post in markdown with Title (link) and key points.
"""
