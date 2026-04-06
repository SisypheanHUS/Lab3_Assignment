"""
Tools module for ReAct Agent.
Provides a collection of callable tools that the agent can use.
"""

from .base import BaseTool
from .travel_tools import GoogleSearchTool, WeatherAPITool, BookingAPITool


def get_all_tools():
    """
    Factory function to get all available tools.
    Returns a list of tool dictionaries ready for the ReActAgent.
    """
    tools = [
        GoogleSearchTool(),
        WeatherAPITool(),
        BookingAPITool(),
    ]
    
    # Convert tool objects to the format expected by ReActAgent
    return [tool.to_dict() for tool in tools]


__all__ = [
    "BaseTool",
    "GoogleSearchTool",
    "WeatherAPITool",
    "BookingAPITool",
    "get_all_tools",
]
