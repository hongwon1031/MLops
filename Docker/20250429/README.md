## 1. Docker 개념 입문

- **Docker란?**
    - 애플리케이션을 컨테이너 단위로 격리해서 실행하는 기술
    - **코드 + 실행환경**을 한 덩어리로 포장해서 어디서나 똑같이 실행
- **Docker 주요 요소**

| 개념 | 설명 |
| --- | --- |
| Dockerfile | 이미지를 만들기 위한 레시피 파일 |
| Docker Image | 실행 가능한 코드/환경 패키지 |
| Docker Container | 이미지를 실행한 인스턴스 |
| Docker Hub | 이미지 저장소 |
| Docker Volume | 데이터 영구 저장소 |

## 2. 실습 진행

| 단계 | 내용 |
| --- | --- |
| 1 | `main.py` 작성 (FastAPI 서버) |
| 2 | `Dockerfile` 작성 |
| 3 | `docker build -t my-fastapi-app .` → 이미지 생성 |
| 4 | `docker run -d -p 8000:8000 --name fastapi-container my-fastapi-app` → 컨테이너 실행 |
| 5 | `docker ps`로 실행 상태 확인 |
| 6 | 브라우저 `http://localhost:8000` 접속 성공 |
| 7 | 에러 발생 시 `docker logs`로 디버깅 연습 |
| 8 | 컨테이너 중지/삭제 (`docker stop`, `docker rm`) 명령어 사용 |

## 3. 터미널과 컨테이너의 차이점

- Docker 컨테이너는 터미널(`cmd`, `powershell`)과 별개로 독립 실행
- 터미널을 종료해도 컨테이너는 계속 실행
- 컨테이너를 종료하려면 `docker stop` 명령어 사용