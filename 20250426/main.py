from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(
    item_id: int,
    q: str = Query(
        ...,
        min_length = 3,
        max_length = 10,
        description = '검색할 키워드를 입력하세요(3~10자)'
    )
):
    return {"item_id" : item_id, "q" : q}
    