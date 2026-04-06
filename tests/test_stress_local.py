import os
import sys
import pytest
from dotenv import load_dotenv

# Add src to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.core.local_provider import LocalProvider

@pytest.mark.parametrize("prompt,expected_min_length", [
    ("Explain what an AI Agent is in one sentence.", 10),
    ("Summarize the history of artificial intelligence in 3 sentences.", 30),
    ("What is the capital of France?", 5),
    ("a" * 10000, 10),  # Extremely long prompt
    ("", 1),  # Empty prompt
])
def test_local_provider_stress(prompt, expected_min_length):
    load_dotenv()
    model_path = os.getenv("LOCAL_MODEL_PATH", "./models/Phi-3-mini-4k-instruct-q4.gguf")
    if not os.path.exists(model_path):
        pytest.skip(f"Model file not found at {model_path}")
    provider = LocalProvider(model_path=model_path)
    try:
        result = provider.generate(prompt)
        content = result["content"]
        assert isinstance(content, str)
        assert len(content) >= expected_min_length
    except Exception as e:
        # Print error for demonstration, but fail the test
        print(f"Error for prompt '{prompt[:50]}...': {e}")
        assert False, f"Provider failed for prompt: {prompt[:50]}..."

def test_local_provider_invalid_model():
    with pytest.raises(FileNotFoundError):
        LocalProvider(model_path="/invalid/path/to/model.gguf")
