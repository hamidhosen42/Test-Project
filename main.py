from fastapi import FastAPI
from pydantic import BaseModel
from db import collection  

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    collection.insert_one(item_dict)
    return {"message": "Item added successfully", "item": item_dict}

@app.get("/items/{name}")
async def get_item(name: str):
    item = collection.find_one({"name": name})
    if item:
        return {"item": item}
    return {"message": "Item not found"}
