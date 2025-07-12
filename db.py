from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")  # Default to localhost if not set

client = MongoClient(MONGO_URI)
db = client["test-db"]  # Your database name
collection = db["test_collection"]  # Your collection name