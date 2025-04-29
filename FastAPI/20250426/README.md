# 📘 FastAPI Day 4 학습 정리 (Path + Query Parameters)

---

## ✅ 학습 목표
- Path Parameter와 Query Parameter를 함께 사용하는 방법을 익힌다.
- Query Parameter의 제약조건 설정 방법을 배운다.
- Query Parameter를 필수로 만드는 방법을 학습한다.

---

## 📌 오늘 학습한 개념

### 1. Path Parameter
- URL 경로 안에 변수를 포함시키는 방법.
- 예: `/items/{item_id}` → item_id는 경로를 통해 받음.

### 2. Query Parameter
- URL 경로 뒤에 `?key=value` 형식으로 전달하는 변수.
- 예: `/items/1?q=banana`
- 선택적으로 사용할 수 있으며 기본값을 줄 수 있다.

### 3. Path + Query 함께 사용하기
```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
- Path로 `item_id`, Query로 `q`를 받는다.

### 4. fastapi.Query를 활용한 제약조건 설정
```python
from fastapi import Query

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = Query(None, min_length=3, max_length=10, description="검색할 키워드를 입력하세요 (3~10자)")):
    return {"item_id": item_id, "q": q}
```
- 최소 3글자, 최대 10글자만 허용.
- Swagger UI에 설명 추가.

### 5. Query Parameter를 필수로 만들기
```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = Query(...)):
    return {"item_id": item_id, "q": q}
```
- `...` (ellipsis)를 사용하면 필수 파라미터로 설정된다.
- 입력하지 않으면 422 에러 발생.

---

## ✅ 오늘 배운 핵심 요약
- Path와 Query를 동시에 받을 수 있다.
- Query에 다양한 제약조건(min_length, max_length 등)을 걸 수 있다.
- `Query(...)`를 통해 필수 Query로 만들 수 있다.
- FastAPI가 URL 구조를 보고 Path/Query를 자동 구분한다.

---

## 📌 다음 학습 예정
- Query Parameter 고급 옵션 (정규식, 다중값 받기 등)
- 응답 커스터마이징 (status_code, response_model 세부 설정)
- 예외 처리 심화 (커스텀 Exception Handler)
- 자동 문서화 커스터마이징 (Swagger / Redoc)

