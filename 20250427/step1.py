from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    description : str = None
    price : float
    
@app.post('/items/', status_code = 201)
def create_item(item : Item):
    return item