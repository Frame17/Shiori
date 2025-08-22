# Shiori likes reading

Shiori is a Deep Research Agent for Machine Learning research papers and blog posts.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Shiori.git
cd Shiori

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Usage

### Command Line Interface

After installation, you can use the `shiori` command directly:

```bash
# Fetch research papers (default: from the last week)
shiori research

# Fetch blog posts (default: from the last week)
shiori blog

# Specify a time period (d = 1 day, w = 1 week, m = 1 month)
shiori research --time d
shiori research --time w
shiori research --time m

shiori blog --time d
shiori blog --time w
shiori blog --time m

# Specify an output file
shiori research --output custom_papers.md
shiori blog --output custom_blogs.md
```

## Telemetry

To run the telemetry server:

```bash
python -m phoenix.server.main serve
```

This will start the telemetry server which helps monitor the agent's performance and behavior.

## Output

The output is a markdown file containing:

- For research papers (default: `papers_summary.md`): Research papers with title, problem, approach, and evaluation
- For blog posts (default: `blog_summary.md`): Blog posts from major AI companies with key points
