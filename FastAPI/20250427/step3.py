from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/custom_response/')
def custom_response():
    content = {'message' : 'This is a custom response'}
    return JSONResponse(content = content, status_code=200)

