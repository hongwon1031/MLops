from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 입력 모델
class Item(BaseModel):
    name : str
    price : float
    description : str = None
    
# 응답 모델(price만 숨기기)
class ItemOut(BaseModel):
    name : str
    description : str = None
    
# POST 요청 처리
@app.post("/items/", response_model=ItemOut, status_code=201)
def create_item(item: Item):
    # 예외 처리
    if item.price < 0:
        raise HTTPException(status_code=400, detail='Price must be non-negative')
    return item