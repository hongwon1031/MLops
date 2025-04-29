from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 입력 모델
class Item(BaseModel):
    name : str
    price : float
    description : str = None

# 응답 모델
class ItemOut(BaseModel):
    name : str
    description : str = None
    
# 가상 DB (딕셔너리)
fake_items = {
    1 : Item(name = 'banana', price = 1000, description = '노란 과일'),
    2 : Item(name = 'apple', price = 1200, description = '빨간 과일')
}

# GET 요청 처리
@app.get("/items/{item_id}", response_model = ItemOut)
def read_item(item_id : int):
    item = fake_items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404,detail = 'Item not found')
    return item