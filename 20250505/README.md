## 🗂️ **1. 로컬 환경 구성 및 테스트**

### 📁 프로젝트 구조

```
bash
복사편집
20250505/
├── app/
│   ├── main.py             ← FastAPI 핵심 코드
│   ├── models.py           ← Pydantic 모델 정의
│   └── .env                ← 환경 변수 설정 (예: project_name)
├── requirements.txt        ← 의존성 목록
├── Dockerfile              ← 컨테이너 이미지 정의
└── docker-compose.yml      ← 서비스 및 포트 설정
```

### 📌 핵심 설정 변경

- **Azure는 반드시 80번 포트만 허용**하므로 아래처럼 수정

### Dockerfile

```docker
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "80:80"  # 로컬 포트도 80으로 통일

```

---

## 🐳 **2. Docker로 이미지 빌드 및 로컬 테스트**

```bash
docker-compose build
docker-compose up -d
```

→ [http://localhost:80](http://localhost/) 으로 접속하여 FastAPI 실행 확인

---

## ☁️ **3. Azure 리소스 구성**

### 3-1. Azure Portal에서 리소스 생성

- ✅ **Azure Container Registry (ACR)**
    
    이름: `6b034container`
    
- ✅ **App Service (Web App for Containers)**
    
    이름: `6b034webapp`
    
- 리전은 동일하게 설정 (예: East US)

---

## 🔐 **4. ACR 접근 권한 설정**

### 방법 1 (현재 사용한 방법): **ACR 관리자 계정 활성화**

1. `6b034container` → **Access Keys**
2. **관리자 사용자 사용 = 활성화(Enabled)**
3. 사용자 이름 + 비밀번호 복사하여 WebApp 배포 설정에 입력

📌 *학습용으로는 간단하고 좋음. 운영에서는 관리 ID 사용 추천*

---

## 📤 **5. Azure ACR에 이미지 업로드**

### 5-1. Azure CLI 설치 확인

```bash
az --versi
```

### 5-2. ACR 로그인

```bash
az acr login --name 6b034container
```

→ 로그인 성공 메시지 확인

### 5-3. 이미지 푸시

```bash
docker tag 20250505-web 6b034container.azurecr.io/fastapi-app:latest
docker push 6b034container.azurecr.io/fastapi-app:latest
```

---

## 🚀 **6. Azure Web App에 컨테이너 배포 설정**

### 설정 위치: App Service → `컨테이너 설정`

| 항목 | 값 |
| --- | --- |
| 이미지 소스 | Azure Container Regis |
| 레지스트리 | 6b034container |
| 이미지 및 태그 | fastapi-app:latest |
| 시작 파일/포트 | 없음 (이미 Dockerfile에 CMD로 명시됨) |
| 포트 | 80 (자동 인식되므로 따로 설정 필요 없음) |

---

## 🌐 **7. 배포 확인**

### 웹앱 기본 도메인 확인:

```
https://6b034webapp-xxxxxxxx.azurewebsites.net/
```

### 정상 동작 예시

- `/` → `{ "message": "FastAPI app is running!" }`
- `/docs` → Swagger UI

---

## 📘 **정리: 기술 스택 및 흐름**

| 구성 요소 | 역할 |
| --- | --- |
| **FastAPI** | Python 웹 서버 |
| **Docker** | 컨테이너화 |
| **docker-compose** | 로컬 멀티 컨테이너 실행 환경 구성 |
| **Azure CLI** | 리소스 연결 및 인증 |
| **Azure Container Registry (ACR)** | 이미지 저장소 |
| **Azure Web App for Containers** | FastAPI 앱을 클라우드에서 실행하는 플랫폼 |
| **브라우저** | 앱에 접속하여 테스트 |

---

## ✅ 최종 결과

- FastAPI 앱을 Docker로 패키징
- Azure ACR에 이미지 업로드
- Azure App Service로 실시간 배포 성공
- 기본 도메인 접속 시 API 및 Swagger 확인 가능