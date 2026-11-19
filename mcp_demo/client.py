import asyncio
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_weather_client():
    # 1. Locate your server file and configure the connection parameters
    server_script = Path(__file__).parent / "server.py"
    
    # We explicitly target the Python interpreter inside your virtual environment (.venv)
    venv_python = Path(__file__).parent / ".venv" / "Scripts" / "python.exe"
    
    server_params = StdioServerParameters(
        command=str(venv_python) if venv_python.exists() else "python",
        args=[str(server_script)],
        env=None
    )
    
    print(f"Connecting to MCP server at: {server_script}...")

    # 2. Establish the Stdio connection channel
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            
            # Initialize the protocol session handshake
            await session.initialize()
            print("Successfully connected to the MCP Server!")

            # 3. Discover available capabilities (List Tools)
            print("\n--- Discovering Tools ---")
            tools_response = await session.list_tools()
            for tool in tools_response.tools:
                print(f" Found Tool: {tool.name}")
                print(f"   Description: {tool.description}")

            # 4. Discover available structural information (List Resources)
            print("\n--- Discovering Resources ---")
            resources_response = await session.list_resources()
            for resource in resources_response.resources:
                print(f" Found Resource: {resource.uri}")
                print(f"   Description: {resource.description}")

            # 5. Call a tool programmatically (Get Temperature)
            print("\n--- Executing Tool Call ---")
            target_city = "Delhi"
            print(f"Calling 'get_temperature' for city='{target_city}'...")
            
            tool_result = await session.call_tool(
                "get_temperature", 
                arguments={"city": target_city}
            )
            
            # The result is returned as structural text content blocks
            print(f"\n{tool_result.content}")  # Display the temperature result
            print(f"\nServer Execution Output:\n{tool_result.content[0].text}")

            # 6. Read a static resource
            print("\n--- Reading Resource Content ---")
            resource_result = await session.read_resource("weather://alerts")
            print(f"Resource Data:\n{resource_result.contents[0].text}")

if __name__ == "__main__":
    # MCP Client sessions use async/await architecture
    asyncio.run(run_weather_client())
