from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["test-db"]  # Your database name
collection = db["test_collection"]  # Your collection name

# Test the connection (optional, for local debugging)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")