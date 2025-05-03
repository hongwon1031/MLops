from fastapi import FastAPI, HTTPException
from pydantic_settings import BaseSettings
from models import Item

class Settings(BaseSettings):
    project_name : str
    
    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(title = settings.project_name)

fake_db = {}

@app.post("/items/", response_model = Item)
def create_item(item:Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail = 'Item already exists')
    fake_db[item.id] = item
    return item

@app.get("/items/{item_id}", response_model = Item)
def read_item(item_id : int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return fake_db[item_id]

@app.put("/items/{item_id}", response_model = Item)
def update_item(item_id : int, item : Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"message": "Item deleted"}
