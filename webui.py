import gradio as gr
import os
from dotenv import load_dotenv
from src.core.gemini_provider import GeminiProvider
from src.agent.agent import ReActAgent
from src.tools import get_all_tools

load_dotenv()

def get_agent():
    provider = GeminiProvider(api_key=os.getenv("GOOGLE_API_KEY"))
    tools = get_all_tools()
    return ReActAgent(llm=provider, tools=tools, max_steps=5)

agent = get_agent()

with gr.Blocks() as demo:
    gr.Markdown("# 🦾 AI Travel Agent (ReAct)\nChat with an agent that can use tools!")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Your message", placeholder="Ask about travel, weather, hotels...")
    clear = gr.Button("Clear")

    history = []

    def user_chat(user_message, chat_history):
        chat_history = chat_history or []
        response = agent.run(user_message)
        chat_history.append((user_message, response))
        return "", chat_history

    msg.submit(user_chat, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: ("", []), None, [msg, chatbot])

demo.launch()
