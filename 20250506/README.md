✅ 2025년 5월 6일 학습 요약 – 스팸 문자 분류 API 프로젝트
🔹 1. ML 모델 학습 (로컬, train_model.ipynb)
데이터셋: SMS Spam Collection (ham/spam)

전처리: TfidfVectorizer로 텍스트를 벡터화

모델: MultinomialNB (나이브 베이즈 분류기)

파이프라인: make_pipeline(TfidfVectorizer(), MultinomialNB())

모델 저장: joblib.dump()로 app/model.pkl로 저장

🔹 2. FastAPI 백엔드 구현
main.py
FastAPI 앱 구성

/predict POST 엔드포인트 구현

predict.py
joblib.load("model.pkl")로 저장된 모델 로딩

입력 메시지를 기반으로 예측 → "spam" 또는 "ham" 반환

schema.py
Pydantic 모델로 요청/응답 구조 정의:

MessageRequest: message(str)

MessageResponse: label(str)

🔹 3. Docker 컨테이너화 및 실행
Dockerfile
python:3.10 베이스 이미지

WORKDIR /app 설정

COPY ./app /app

pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

requirements.txt
fastapi, uvicorn, scikit-learn, pandas, joblib

실행 절차
bash
복사
편집
docker build -t spam-api .
docker run -d -p 8000:80 spam-api
🔹 4. Azure에 Docker 이미지 배포
ACR 사용
기존 6b034container ACR에 docker push로 이미지 업로드

bash
복사
편집
docker tag spam-api 6b034container.azurecr.io/spam-api:latest
docker push 6b034container.azurecr.io/spam-api:latest
Web App for Containers
새 Web App 리소스 생성

ACR 이미지 연결, 포트 80 설정

배포 완료 후 https://<webapp>.azurewebsites.net/docs 접속 확인

🔹 5. Swagger 테스트 완료
/predict 엔드포인트에 문장 입력

"spam" 또는 "ham" 응답 확인

📚 오늘의 핵심 학습 포인트
영역	핵심 내용
머신러닝	텍스트 분류, TF-IDF, 나이브베이즈, 파이프라인 저장
백엔드	FastAPI REST API 작성 및 모델 예측 로직 구현
도커	Dockerfile 작성, 이미지 빌드/실행
Azure	ACR 이미지 업로드, WebApp 컨테이너 배포