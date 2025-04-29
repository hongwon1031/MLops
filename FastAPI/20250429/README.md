## ✅ 오늘의 학습 목표

- FastAPI 요청/응답/에러 흐름 완벽 이해
- 다양한 커스텀 예외 상황 처리
- 종합 실습을 통해 서버 흐름 스스로 구현

---

## 📌 오늘 배운 내용 요약

### 1. FastAPI 에러 핸들링 심화

- `HTTPException` 기본 사용법 복습
- 커스텀 예외 클래스 (`ZeroPriceException`, `ForbiddenNameException`) 직접 정의
- `@app.exception_handler`를 통해 커스텀 예외별로 핸들러 분리
- 클라이언트 요청 오류에 따라 다른 HTTP 상태코드(400, 403, 404) return

### 2. FastAPI 요청/응답 흐름 정리

- 요청 수신 → 경로 매칭 → 타입 파싱 → 함수 실행 → 응답 생성 → 전송
- Pydantic 모델을 통한 요청 Body 타입 검증
- Path Parameter와 Query Parameter 자동 타입 변환
- 에러 발생 시 FastAPI가 자동으로 JSON 형태 응답 생성

---

## 🛠️ 종합 실습: 미니 서버 구축

- **POST** `/products/` : 상품 등록
    - 이름이 "admin"이면 403 Forbidden 에러 발생
    - 가격이 0원이면 400 Bad Request 에러 발생
- **GET** `/products/{product_id}` : 상품 조회
    - 존재하지 않는 상품 조회 시 404 Not Found 에러 발생
- **커스텀 예외 핸들러** 두 종류 성공적으로 등록 및 동작 확인
- Swagger UI를 통한 직접 테스트 완료