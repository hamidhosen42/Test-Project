from fastapi import FastAPI
from pydantic import BaseModel
from db import collection
from bson import ObjectId  # Import ObjectId from bson

app = FastAPI()

# Pydantic model for input data
class Item(BaseModel):
    name: str
    description: str

# Function to convert ObjectId to string
def item_to_dict(item):
    item["_id"] = str(item["_id"])  # Convert ObjectId to string
    return item

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    result = collection.insert_one(item_dict)
    # Optionally, you can return the inserted ID
    return {"message": "Item added successfully", "item_id": str(result.inserted_id)}

@app.get("/items/{name}")
async def get_item(name: str):
    item = collection.find_one({"name": name})
    if item:
        return {"item": item_to_dict(item)}  # Convert ObjectId to string
    return {"message": "Item not found"}
