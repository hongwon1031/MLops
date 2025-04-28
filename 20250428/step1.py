from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/items/{item_id}')
def read_item(item_id : int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail = '아이템이 없음')
    return {'item_id' : item_id}