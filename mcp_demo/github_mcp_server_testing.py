import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 1. PASTE YOUR GITHUB TOKEN HERE (or set it in your system env)
GITHUB_TOKEN = ""  # Replace with your actual GitHub Personal Access Token

async def run_github_mcp_client():
    if GITHUB_TOKEN == "your_ghp_token_here":
        print("❌ Error: Please update the GITHUB_TOKEN variable with your actual token!")
        return

    print("Connecting to official GitHub MCP Server via Docker...")

    # 2. Tell the client to call Docker to execute the pre-built server image
    server_params = StdioServerParameters(
        command="docker",
        args=[
            "run", 
            "-i", 
            "--rm", 
            "-e", f"GITHUB_PERSONAL_ACCESS_TOKEN={GITHUB_TOKEN}", 
            "ghcr.io/github/github-mcp-server"
        ]
    )

    # 3. Create the standard connection stream
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            
            # Handshake
            await session.initialize()
            print("Successfully connected to the remote GitHub Server!")

            # 4. Discover the production tools GitHub built
            print("\n--- Discovering Live GitHub Tools ---")
            tools_response = await session.list_tools()
            print(f"Total tools exposed by GitHub: {len(tools_response.tools)}")
            
            # Print out the first 5 tools so we can see what it can do
            for tool in tools_response.tools[:5]:
                print(f" 🛠️ Tool Name: {tool.name}")
                print(f"     Description: {tool.description}")

            # 5. Programmatically call a real tool!
            # Let's ask the server to pull down info about our own user profile
            print("\n--- Running GitHub Tool Call ---")
            print("Calling 'get_me' to retrieve authenticated profile metrics...")
            
            try:
                result = await session.call_tool("get_me", arguments={})
                print(f"\nExecution Response from GitHub:\n{result.content[0].text}")
            except Exception as e:
                print(f"Tool execution failed: {e}")

if __name__ == "__main__":
    # Ensure Docker Desktop is running on your Windows machine before executing
    asyncio.run(run_github_mcp_client())