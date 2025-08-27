"""
Prompts for Shiori to do her homework.
"""

RESEARCH_PAPERS_PROMPT = """
Find and rank the top {count} machine learning research papers related to **Large Language Models (LLMs) and Deep NLP** {time_period}.  

Steps:  
1. Query the tools for the impactful and influential papers in machine learning, belonging to topics such as:
   - LLM publications (transformers, mixture-of-experts, scaling laws)  
   - Training/fine-tuning methods (RLHF, model alignment, instruction-tuning, distillation)  
   - Efficiency & deployment (inference optimization, quantization, retrieval augmentation)  
2. Filter out the result that are not {time_period}.
3. Rank the top 5 papers by the sagnificance, authority and relevance to LLMs/Deep NLP.  
4. Output them in the following format:

**Title**:
**Link**:
**Problem**:
**Approach**:
**Evaluation**:

Guidelines:  
- Always use filtering capabilities of the available tools to narrow down the search to the most relevant results.
- All papers MUST be {time_period}. Today's date: {date_now}.
- Focus only on ML papers, emphasizing LLMs and Deep NLP.  
"""

BLOG_POSTS_PROMPT = """
Search for recent blog posts from top AI companies, such as OpenAI, Anthropic, Google DeepMind, 
Meta, Mistral, DeepSeek, xAI, Alibaba, ByteDance and JetBrains {time_period}.
Summarize each post in markdown with Title (link) and key points.
"""
