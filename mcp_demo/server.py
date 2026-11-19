# D:\MyProject\python\mcp_demo\server.py
from fastmcp import FastMCP
import random

# Initialize FastMCP Server
mcp = FastMCP("Local Weather Service")

# Expose a Tool
@mcp.tool()
def get_temperature(city: str) -> str:
    """Fetches the current temperature for a given city."""
    mock_temp = random.randint(15, 35)
    return f"The current temperature in {city} is {mock_temp}°C."

# Expose a Resource
@mcp.resource("weather://alerts")
def get_weather_alerts() -> str:
    """Provides a list of active emergency weather alerts."""
    return "ALERT: High wind warning active for coastal regions until 9:00 PM."

if __name__ == "__main__":
    # Crucial Change: Force clean stdio mode for programmatic clients
    mcp.run(transport="stdio")
