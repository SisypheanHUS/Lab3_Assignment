import os
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Generator

class LLMProvider(ABC):
    """
    Abstract Base Class for LLM Providers.
    Supports OpenAI, Gemini, and Local models.
    """

    def __init__(self, model_name: str, api_key: Optional[str] = None):
        self.model_name = model_name
        self.api_key = api_key

    @abstractmethod
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> Dict[str, Any]:
        """
        Produce a non-streaming completion.
        Returns:
            Dict containing:
            - content: The response text
            - usage: { 'prompt_tokens', 'completion_tokens' }
            - latency_ms: Response time
        """
        pass

    @abstractmethod
    def stream(self, prompt: str, system_prompt: Optional[str] = None) -> Generator[str, None, None]:
        """Produce a streaming completion."""
        pass

    def generate_response(self, system_prompt: str, history: List[Dict[str, str]], prompt: str) -> str:
        """
        Generate a response using the conversation history.
        This is a convenience method for agent/chatbot that handles multi-turn conversations.
        
        Args:
            system_prompt: System/context prompt
            history: List of previous messages with 'role' and 'content'
            prompt: User's current input
            
        Returns:
            The LLM's response text
        """
        # Build messages: system + history + current prompt
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.extend(history)
        messages.append({"role": "user", "content": prompt})
        
        # For now, use generate() with just the current prompt and system
        # A subclass can override this for better history handling
        response = self.generate(prompt, system_prompt)
        return response["content"]
