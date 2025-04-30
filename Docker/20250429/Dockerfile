# 1. 사용할 베이스 이미지 지정
FROM python:3.11-slim

# 2. 작업 디렉토리 생성
WORKDIR /app

# 3. 현재 폴더(소스 코드)를 컨테이너 안으로 복사
COPY ./main.py /app

# 4. 필요한 패키지 설치
RUN pip install fastapi uvicorn

# 5. 컨테이너가 실행될 때 명령어
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

