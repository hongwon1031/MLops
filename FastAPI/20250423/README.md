# 📅 FastAPI 입문 Day 1 - 복습 정리

## ✅ 오늘의 주요 학습 목표
- FastAPI의 기본 개념 이해
- GET, POST API 작성 및 Swagger UI 테스트
- Path Parameter & Query Parameter 활용
- JSON 데이터 처리 및 자동 유효성 검사 경험

---

## 🧠 핵심 개념 요약

### ✅ FastAPI란?
- Python 기반 고성능 웹 프레임워크 (ASGI)
- 자동 문서화 (Swagger, ReDoc)
- 비동기 지원 (`async def`)
- 타입 기반 입력 검증 (`Pydantic` 사용)

### ✅ GET vs POST
| 항목 | GET | POST |
|------|-----|------|
| 용도 | 데이터 조회 | 데이터 생성, 제출 |
| 요청 위치 | URL 경로/쿼리 | 본문(JSON) |
| Swagger UI 입력 위치 | URL + 입력창 | JSON 입력창 |

### ✅ Swagger UI
- `/docs` 경로에서 자동 문서 확인 가능
- `Try it out` → `Execute` 시 실제 HTTP 요청 발생

### ✅ 주요 기능 정리
| 기능 | FastAPI가 자동으로 해주는 일 |
|------|--------------------------|
| JSON 파싱 | 본문 데이터를 Python 객체로 변환 |
| 유효성 검사 | Pydantic 타입 기반으로 오류 검출 |
| 응답 변환 | Python 객체 → JSON 응답 처리 |
| 문서화 | 모든 경로 + 요청/응답 구조 자동 생성 |

---

## 🛠️ 실습 정리

### 🔹 `GET /` 구현
```python
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}
```

### 🔹 `GET /items/{item_id}` with Query
```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

### 🔹 `POST /items/` with JSON
```python
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return {
        "received_name": item.name,
        "received_price": item.price,
        "offer_status": item.is_offer
    }
```

---

## ✅ 오늘의 나의 인사이트
- FastAPI는 단순한 JSON 처리를 넘어서 구조화된 백엔드 구축에 매우 유리하다.
- Swagger를 통한 테스트는 문서화 + 실시간 실행이 동시에 가능해서 생산성이 매우 높다.
- Pydantic 기반 유효성 검사와 자동 응답 구조는 실무에서 큰 강점이 될 수 있다.

---

## 🔜 다음 학습 예고 (Day 2)
- `response_model`로 응답 형식 강제
- `status_code`로 상태 관리
- `HTTPException`으로 예외 처리 구조 설계
- 실전형 라우팅 패턴 및 API 설계

