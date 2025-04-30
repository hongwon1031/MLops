# 📚 정리
## ✅ 오늘의 핵심 목표

> **FastAPI + Redis를 Docker Compose로 다중 컨테이너 구성 및 연동**
> 

| 단계 | 실습 내용 | 달성 여부 |
| --- | --- | --- |
| Docker Compose 개념 이해 | 왜 필요한지, 구조, 명령어 | ✅ |
| `main.py` 작성 | FastAPI + Redis 연결 API | ✅ |
| `requirements.txt` 구성 | FastAPI + redis 패키지 정리 | ✅ |
| Dockerfile 작성 | FastAPI 서버 빌드 설정 | ✅ |
| docker-compose.yml 작성 | web + redis 컨테이너 구성 | ✅ |
| 빌드 및 실행 | `docker-compose build` + `up -d` | ✅ |
| Redis 통신 확인 | `/set`, `/get` API 테스트 | ✅ |
| 오타 디버깅 | `0,0,0,0` → `0.0.0.0`, 연결 거부 해결 | ✅ |

| 개념 | 요약 |
| --- | --- |
| Docker Compose | 여러 컨테이너를 `.yml` 하나로 묶어서 실행 |
| `depends_on` | 실행 순서만 보장 (준비 완료 보장은 ❌) |
| `CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]` | 컨테이너 외부 접속 위해 반드시 필요 |
| `docker-compose build` | 이미지 재빌드 (삭제 없이 반영됨) |
| `docker-compose up -d` | 전체 컨테이너 백그라운드 실행 |

---

# 🐞 실습중 발생한 에러

## ❌ 에러 1: `port is already allocated`

```bash
Bind for 0.0.0.0:8000 failed: port is already allocated
```

### 🔍 원인

- 8000번 포트를 이미 다른 컨테이너나 로컬 서버가 사용 중

### ✅ 해결 방법

- 기존 컨테이너 중지
    
    ```bash
    docker stop 기존 컨테이너명
    ```
    
- 또는 `docker-compose.yml`에서 포트 변경
    
    ```yaml
    ports:
    	-"8001:8000"
    ```
    

---

## ❌ 에러 2: `decode_response` 잘못된 인자

```bash
TypeError: Redis.__init__() got an unexpected keyword argument 'decode_response'
```

### 🔍 원인

- 오타
    - `decode_response=True` ❌
    - `decode_responses=True`✅

## ❌ 에러 3: Redis 연결 오류 
`[Errno -2] Name or service not known`

### 🔍 원인

- FastAPI 서버가 Redis보다 먼저 연결을 시도함
    
    → Compose는 실행 순서만 보장, 준비 완료는 보장 ❌
    

### ✅ 해결 방법

- 일시적 대기 추가:
    
    ```bash
    import time
    time.sleep(3)
    ```