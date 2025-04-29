from fastapi import FastAPI

# FastAPI 인스턴스 생성
app = FastAPI()

# 루트 경로에 GET 요청을 보냈을 때 실행될 함수
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

from pydantic import BaseModel  # 👈 추가된 부분

# ✅ 입력 데이터 모델 정의
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None  # 선택 사항 (Optional)

# ✅ POST 요청 처리 함수
@app.post("/items/")
def create_item(item: Item):
    return {
        "received_name": item.name,
        "received_price": item.price,
        "offer_status": item.is_offer
    }
