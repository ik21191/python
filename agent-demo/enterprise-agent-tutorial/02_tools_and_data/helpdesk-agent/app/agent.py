import os
import uuid
from google.cloud import firestore
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

# Replace with your actual Google Cloud Project ID
project_id = "test-ai-poc-513207" 
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

# Initialize Firestore client

# Replace with your actual Google Cloud Project ID and Database ID
project_id = "test-ai-poc-513207"
database_id = "devices"  # Change this to your specific database ID

db = firestore.Client(project=project_id, database=database_id)
def get_device_status(device_id: str) -> str:
    """Retrieve the status and warranty information for a specific company device."""
    doc_ref = db.collection("devices").document(device_id.upper())
    doc = doc_ref.get()
    
    if not doc.exists:
        return f"Device {device_id} not found in the asset database."
    
    device = doc.to_dict()
    return f"Device: {device.get('model')}\nStatus: {device.get('status')}\nWarranty: {device.get('warranty')}"

def create_it_ticket(user: str, issue: str) -> str:
    """Create a support ticket in the IT Helpdesk system."""
    ticket_id = f"TICKET-{str(uuid.uuid4())[:8].upper()}"
    
    # Save the ticket to Firestore
    db.collection("tickets").document(ticket_id).set({
        "user": user,
        "issue": issue,
        "status": "Open",
        "ticket_id": ticket_id
    })
    
    return f"Successfully created ticket {ticket_id}. Our IT team will look into it shortly."

# Attach the tools to the agent
root_agent = Agent(
    name='it_helpdesk_agent',
    model=Gemini(
        model="gemini-3.8-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are a highly skilled and friendly IT Helpdesk Assistant for a large enterprise. "
        "Your primary goal is to help employees troubleshoot basic IT issues. "
        "You have access to an Asset Management System via the provided tools. "
        "If a user asks about a device, ALWAYS use the get_device_status tool. "
        "If a user needs to report a broken device or an issue you cannot solve, use the create_it_ticket tool. "
        "Be concise and professional."
    ),
    tools=[get_device_status, create_it_ticket]
)

app = App(
    root_agent=root_agent,
    name="app",
)