from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """
    Abstract base class for all tools used by the ReAct Agent.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args, **kwargs) -> str:
        """
        Execute the tool and return a string result.
        This is what the agent will call.
        """
        pass

    def to_dict(self) -> Dict[str, Any]:
        """Convert this tool to the format expected by ReActAgent."""
        return {
            "name": self.name,
            "description": self.description,
            "func": self.run,
        }
