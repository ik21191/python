import os
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

# Replace with your actual Google Cloud Project ID
project_id = "test-ai-poc-513207" 
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
root_agent = Agent(
    name='it_helpdesk_agent',
    model=Gemini(
        model="gemini-3.8-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are a highly skilled and friendly IT Helpdesk Assistant for a large enterprise. "
        "Your primary goal is to help employees troubleshoot basic IT issues, such as password resets, "
        "software installations, and network connectivity problems. "
        "Be concise, polite, and prioritize security best practices. "
        "If an issue seems too complex, politely inform the user that a human technician will need to take over."
    ),
)
app = App(
    root_agent=root_agent,
    name="app",
)