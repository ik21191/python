import os
from google.cloud import firestore

# Replace with your actual Google Cloud Project ID and Database ID
project_id = "test-ai-poc-513207"
database_id = "devices"  # Change this to your specific database ID

db = firestore.Client(project=project_id, database=database_id)

# Create the device document
db.collection("devices").document("LAPTOP-002").set({
    "model": "ThinkPad T14",
    "status": "Needs Repair",
    "warranty": "Expired"
})
print(f"Successfully seeded LAPTOP-002 into Firestore database: {database_id}!")
