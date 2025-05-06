from fastapi import FastAPI
from schema import MessageRequest,MessageResponse
from predict import predict_spam

app = FastAPI()

@app.post("/predict", response_model = MessageResponse)
def predict(request : MessageRequest):
    result = predict_spam(request.message)
    return MessageResponse(label = result)
