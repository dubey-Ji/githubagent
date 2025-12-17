from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
import asyncio
import os

load_dotenv()

GITHUB_PERSONAL_ACCESS_TOKEN = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

client = MultiServerMCPClient(
    {
        "github": {
            "transport": "stdio",
            "command": "/Users/ashutoshdubey/Desktop/github-mcp-server/github-mcp-server",
            "args": ["stdio"],
            "env": {
                "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_PERSONAL_ACCESS_TOKEN
            }
      }
    }
)

async def agent():
    tools = await client.get_tools()

    agent = create_agent(model=llm,tools=tools)


    prompt = ChatPromptTemplate.from_template("Tell me the number of repositories in organization: Xemailverify")

    result = await agent.ainvoke({
        "messages": [HumanMessage(content="What is the number of repositories in organization: Xemailverify")]
    })
    print(result)

asyncio.run(agent())

# Design
# Orchestra Agent
# Github Agent
# MCP Client
# Github MCP server