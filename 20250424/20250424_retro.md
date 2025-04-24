# 📘 FastAPI Day 2 학습 정리 (POST & GET 요청 흐름)

---

## ✅ 학습 목표
- FastAPI의 요청/응답 전체 흐름을 이해한다.
- POST 및 GET 요청 처리 방식을 실습한다.
- Pydantic 모델과 response_model의 역할을 명확히 구분한다.

---

## 📌 POST 요청 실습 코드 구조

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None

class ItemOut(BaseModel):
    name: str
    description: str = None

@app.post("/items/", response_model=ItemOut, status_code=201)
def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price must be non-negative")
    return item
```

---

## 📌 GET 요청 실습 코드 구조

```python
fake_items = {
    1: Item(name='banana', price=1000, description='노란 과일'),
    2: Item(name='apple', price=1200, description='빨간 과일')
}

@app.get("/items/{item_id}", response_model=ItemOut)
def read_item(item_id: int):
    item = fake_items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return item
```

---

## 🔍 요청 흐름: FastAPI vs Python 역할

| 단계 | FastAPI 역할 | Python 코드 역할 |
|------|---------------|-------------------|
| 서버 시작 | `uvicorn main:app --reload` 실행 | - |
| URL 매핑 | @app.get()/@app.post()으로 라우팅 등록 | - |
| 요청 수신 | 클라이언트 → URL 요청 수신 | - |
| 파라미터 파싱 | URL(Path) 또는 JSON Body 자동 변환 | - |
| 함수 실행 | 등록된 함수 호출 | 조건 처리 및 리턴 수행 |
| 예외 발생 | `HTTPException` 자동 포맷 처리 | 예외 발생은 내가 raise |
| 응답 처리 | response_model 필터링 + JSON 직렬화 | 리턴 객체 작성 |
| 응답 전송 | JSON 응답 + 상태코드 전송 | - |

---

## 📦 FastAPI 내부 처리 요약

- `@app.get(...)`, `@app.post(...)` → URL과 함수 매핑 등록
- 요청 시: 파라미터와 JSON body → 타입 힌트 기반 자동 변환
- 리턴값이 Pydantic 모델이면 `.dict()` → JSON 변환
- `response_model`로 필드 필터링
- `JSONResponse`로 감싸서 클라이언트에 응답 전송

---

## ✅ 개념 요약

### Pydantic vs FastAPI
- **Pydantic(BaseModel)**: 데이터 구조 정의 + 타입 유효성 검사
- **FastAPI**: 전체 요청 흐름 자동화 (라우팅, 타입 변환, 응답 직렬화 등)

### 응답 모델
- `response_model=ItemOut` → 응답에 포함할 필드를 제한

### 타입 힌트 자동 처리
- Path Parameter 또는 JSON Body의 값을 자동으로 변환 (`str` → `int`, `float`, etc.)
- 실패 시 → `422 Unprocessable Entity` 자동 응답

### 예외 처리
- `raise HTTPException(...)` → FastAPI가 JSON 에러 응답 생성

---

## ✅ 오늘 배운 핵심

- FastAPI는 요청 수신부터 응답 전송까지 거의 모든 과정 자동화
- 함수 내부는 Python 로직, 외부 흐름은 FastAPI가 관리
- POST 요청은 Pydantic 모델로 JSON body 파싱 후 처리
- 응답은 JSON으로 자동 직렬화되며, `response_model`로 필터링 가능

---

## 📌 다음 학습 예정
- Query Parameter 실습 (예: `/items?q=banana`)
- 필수/선택 파라미터 처리
- 모듈 분리 및 구조 정리

