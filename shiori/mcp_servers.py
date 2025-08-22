"""
MCP Server Configuration

Contains the configuration for MCP servers used by Shiori.
"""

from mcpadapt.core import StdioServerParameters
from smolagents import DuckDuckGoSearchTool, MCPClient


def get_arxiv_client() -> MCPClient:
    server_params = StdioServerParameters(
        command="uv",
        args=[
            "tool",
            "run",
            "arxiv-mcp-server",
            "--storage-path",
            "/Users/serhii.fedusov/Shiori/papers",
        ],
    )
    return MCPClient(server_params)


def get_huggingface_client() -> MCPClient:
    server_params = {
        "url": "http://127.0.0.1:11112/mcp",
        "transport": "streamable-http",
    }
    return MCPClient(server_params)


def get_all_mcp_tools():
    tools = []

    arxiv_client = get_arxiv_client()
    tools.extend(arxiv_client.get_tools())

    hf_client = get_huggingface_client()
    tools.extend(hf_client.get_tools())

    tools.append(DuckDuckGoSearchTool())
    return tools
