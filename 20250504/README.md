# 🎯 학습 목표

> FastAPI로 만든 CRUD API 서버를 Docker로 컨테이너화 하고,
Github Actions를 통해 CI 자동화 파이프라인을 구축
> 

---

## 1️⃣ FastAPI로 CRUD 구현

### ✅ 개념 요약

- FastAPI : 비동기 기반 Python 웹 프레임워크
- CRUD : Create, Read, Update, Delete 동작을 모두 포함한 REST API

### ✅ 주요 코드 구조

```python
# models.py
class Item(BaseModel):
    id: int
    name: str
    description: str

# main.py
app = FastAPI(title=settings.project_name)

@app.post("/items/")
@app.get("/items/{item_id}")
@app.put("/items/{item_id}")
@app.delete("/items/{item_id}")
```

- `pydantic` 모델로 요청 바디 구조화
- `FastAPI` 라우터로 CRUD 구성
- Swagger 문서 자동 생성 (`/docs`)

---

## 2️⃣ Docker로 컨테이너화

### ✅ 핵심 개념

- Docker는 실행 환경을 패키징해서 어디서든 동일하게 실행되도록 도와줌
- `.env` 파일로 환경 변수 분리

### ✅ 작성 파일

**📄 Dockerfile**

```python
FROM python:3.10-slim
WORKDIR /app
COPY ./app /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

📄 **docker-compose.yml**

```python
version: "3"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - ./app/.env

```

### 실행 명령어

```python
docker-compose build       # 이미지 빌드
docker-compose up -d       # 컨테이너 실행
```

> 브라우저에서 `localhost:8000` 접속
`localhost:8000/docs`로 API 테스트 가능
> 

---

## 3️⃣ GitHub Actions로 CI 자동화

### ✅ 핵심 개념

- CI - 코드 변경 시 자동으로 테스트 / 빌드
- GitHub Actions - `.yml` 파일 기반의 Github 자동화 도구

### ✅ 폴더 구조

```markdown
MLops/
├── 20250503/
└── .github/
    └── workflows/
        └── ci.yml
```

### ✅ 주요 워크플로우(`.yml`)

```yaml
on:
  push:
    branches: [ "main" ]

jobs:
  build-and-test:
    steps:
      - checkout 코드
      - Python 환경 세팅
      - 의존성 설치 + 모델 import 테스트
      - Docker 이미지 빌드

```

### ✅ 실행 결과

- `git push` 시 GitHub Actions 자동 실행
- `Actions` 탭에서 로그 확인 가능
- 성공 시 정상적으로 빌드 및 테스트 통과

---

## 📌 핵심 요약

| 항목 | 내용 |
| --- | --- |
| FastAPI | REST API 서버 구현 (CRUD) |
| Docker | 실행 환경을 이미지로 패키징 |
| Docker Compose | 컨테이너 실행 자동화 |
| .env | 환경 변수 외부화 |
| GitHub Actions | 코드 푸시 → 테스트 + 빌드 자동화 (CI) |
| 결과 | FastAPI → Docker → GitHub Actions 연동까지 완료 🎉 |