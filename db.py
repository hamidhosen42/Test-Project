from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("mongodb+srv://hamid42:5wmsu65GhQOkUcea@test-db.apjrc6g.mongodb.net/?retryWrites=true&w=majority&appName=test-db")  # Default to localhost if not set

client = MongoClient(MONGO_URI)
db = client["test-db"]  # Your database name
collection = db["test_collection"]  # Your collection name