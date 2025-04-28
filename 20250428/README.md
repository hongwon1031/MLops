# 🎯 오늘 핵심 학습 주제

- FastAPI 기본 에러 처리 흐름 이해
- `raise` 키워드를 통한 예외 발생
- 커스텀 예외와 커스텀 핸들러 작성 방법 학습

---

## 📌 FastAPI 에러 핸들링 흐름

1. 사용자가 잘못된 요청을 보내거나
2. 서버 코드 내부에서 `raise HTTPException`을 호출하면
3. FastAPI는 자동으로 **상태코드 + Json 에러 메시지**를 만들어서 응답

---

## 📌 `raise` 동작

- Python에서 `raise`는 에러를 강제로 발생시키는 키워드
- FastAPI에서는 `raise HTTPException` 또는 `raise CustomException`으로 에러를 발생시켜야함
- raise가 호출되면 프로그램 흐름은 즉시 멈추고 예외 처리 시작

---

## 📌 커스텀 예외 처리 흐름

1. `Exception` 클래스를 상속해 나만의 예외 클래스 정의
2. `@app.exception_handler(MyCustomException)` 데코레이터로 핸들러 등록
3. 특정 상황에서 `raise MyCustomException()`을 호출
4. FastAPI가 자동으로 핸들러 함수를 호출해서 **직접 정의한 응답**을 만들어줌


---
# ❓ 헷갈리는 개념

## 1. `@app.exception_handler(MyCustomException)` 의 의미는?

### 등록 단계

`@app.exception_handler(MyCustomException)`는 "**나중에 만약 MyCustomException이 터지면 이 함수(my_custom_exception_handler)를 호출해라**” 라고 FastAPI에 등록하는 것

### 실행 단계

코드가 돌아가다 정말 `raise MyCustomException`이 발생하면, FastAPI가 그걸 감지하고 → 등록된 핸들러를 호출

## 2. `async def my_custom_exception_handler(request: Request, exc: MyCustomException)`

### `async def`란?

- async def는 비동기 함수
- FastAPI는 비동기(Async) 프로그래밍을 지원하는 웹 프레임워크라서, 요청을 처리할 때 멈추지 않고 빠르게 다른 요청도 처리할 수 있게 함

| 파라미터 | 설명 |
| --- | --- |
| `request: Request` | 사용자가 보낸 요청 전체(Request 객체) |
| `exc: MyCustomException` | 발생한 예외 객체 (여기에 name이 저장되어 있음) |

> **`@app.exception_handler(MyCustomException)`**
➔ MyCustomException이 발생했을 때 my_custom_exception_handler 함수를 호출하겠다고 FastAPI에 등록.
> 

> **`async def my_custom_exception_handler(request, exc)`**
➔ 발생한 에러(exc 객체)를 받아서 비동기로 JSON 응답을 만들어 반환.
>

# ✅ 최종 요약

> **FastAPI 에러 핸들링은 raise로 오류를 발생시키고, 커스텀 핸들러로 자유롭게 응답을 제어할 수 있다.**
>