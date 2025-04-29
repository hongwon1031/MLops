from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# 커스텀 예외 클래스
class MyCustomException(Exception):
    def __init__(self, name : str):
        self.name = name

# 커스텀 예외 핸들러 등록
@app.exception_handler(MyCustomException)
async def my_custom_exception_handler(request : Request, exc : MyCustomException):
    return JSONResponse(
        status_code=418,
        content = {'message' : f'오! {exc.name}에 문제가 발생했어요!'},
    )

# 라우터
@app.get('/custom_error/{name}')
def custom_error(name : str):
    if name == 'error':
        raise MyCustomException(name = name)
    return {'name' : name}