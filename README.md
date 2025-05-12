# FastAPI → Docker → Kubernetes 커리큘럼

## ✅ 전체 기간 목표
FastAPI 서버를 Docker로 감싸고 azure를 통한 웹 배포까지 실행

---


# 📅 주차별 세부 계획

## FastAPI
### 🛠️ 4월 24일 (수)

- FastAPI 기본 구조 이해
- FastAPI 인스턴스 생성 및 Hello World API 작성

### 🛠️ 4월 25일 (목)

- Path Parameter 처리 (/items/{item_id})
- Query Parameter 처리 (/items/?q=value)

### 🛠️ 4월 26일 (금)

- Pydantic 모델을 이용한 요청/응답 데이터 구조화
- 데이터 유효성 검사 및 타입 자동 변환

### 🛠️ 4월 27일 (토)

- POST 요청 처리 실습
- response_model을 통한 응답 데이터 필터링
- 상태 코드 변경 (status_code=201)

### 🛠️ 4월 28일 (일)

- HTTPException을 통한 기본 에러 핸들링
- 커스텀 예외 클래스 정의 및 커스텀 핸들러 작성
- 전체 요청-응답-에러 처리 흐름 마스터

### 🛠️ 4월 29일 (월)

- FastAPI 요청/응답/에러 처리 최종 복습
- FastAPI 종합 미니 프로젝트 (API 서버 직접 설계)

---

## Docker
### 🛠️ 4월 30일 (화)

- FastAPI 전체 흐름 요약 정리
- Docker 개념 이론 준비 (이미지, 컨테이너, Dockerfile 이해)

### 🛠️ 5월 1일 (수)

- Docker 설치 및 환경 구축
- docker build, docker run, docker stop 명령어 실습
- FastAPI 서버를 Docker로 패키징

### 🛠️ 5월 2일 (목)

- Docker Compose 이론 학습
- Compose로 FastAPI + Redis 다중 컨테이너 구성 실습

### 🛠️ 5월 3일 (금)

- FastAPI + DB 프로젝트를 Docker Compose로 구축
- 실제 서비스 흐름과 비슷하게 실습

### 🛠️ 5월 4일 (토)

- Docker 전체 복습
- 작은 미니 프로젝트 (FastAPI + DB + Docker Compose로 구축)

---

## Kubernetes

### 🛠️ 5월 5일 (일)

- Kubernetes 핵심 개념 학습 (Pod, ReplicaSet, Deployment, Service)
- Kubernetes용 YAML 파일 작성법 학습

### 🛠️ 5월 6일 (월)

- Minikube 설치 및 로컬 Kubernetes 클러스터 생성
- Dockerized FastAPI 앱을 Kubernetes에 배포
- kubectl 명령어 실습 (apply, get, describe)

### 🛠️ 5월 7일 (화)

- FastAPI → Docker → Kubernetes 전체 흐름 최종 복습
- 최종 미니 프로젝트 리허설
