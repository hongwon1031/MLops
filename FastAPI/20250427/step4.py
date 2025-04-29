from fastapi.responses import JSONResponse
from fastapi import FastAPI

app = FastAPI()

@app.get('/custom_header/')
def custom_header_response():
    content = {'message' : 'This is a response with custom headers'}
    headers = {
        'X-Custom-Header' : 'MyCustomValue',
        'X-Another-Header' : 'AnotherValue'
    }    
    return JSONResponse(content=content,headers=headers,status_code=200)