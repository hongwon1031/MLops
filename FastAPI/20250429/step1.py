from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

fake_items = {
    1 : {'name' : 'banana', 'price' : 1000},
    2 : {'name' :  'apple', 'price' : 1200}
}

# 가격이 0 이하일때 발생하는 예외
class ZeroPriceException(Exception):
    def __init__(self, item_name : str):
        self.item_name = item_name

# 이름이 금지어일 때 발생하는 예외
class ForbiddenNameException(Exception):
    def __init__(self,forbidden_name : str):
        self.forbidden_name = forbidden_name
 
# ZeroPriceException 핸들러
@app.exception_handler(ZeroPriceException)
async def zero_price_exception_handler(request:Request, exc : ZeroPriceException):
    return JSONResponse(
        status_code = 400,
        content = {'detail' : f'{exc.item_name}의 가격이 0 이하입니다! 올바른 가격을 입력하세요.'}
    )

# ForbiddenNameException 핸들러
@app.exception_handler(ForbiddenNameException)
async def forbidden_name_exception_handler(request : Request, exc : ForbiddenNameException):
    return JSONResponse(
        status_code=400,
        content = {'detail' : f'{exc.forbidden_name}은 사용할 수 없는 이름입니다'}
    )

# 아이템 조회(GET)
@app.get("/itmes/{item_id}")
def get_item(item_id : int):
    item = fake_items.get(item_id)
    if not item:
        raise HTTPException(status_code = 400, detail = 'item not found')
    return item

# 아이템 생성
@app.post("/items/")
def create_item(name : str, price : int):
    # 금지된 이름 체크
    if name.lower() == 'admin':
        raise ForbiddenNameException(forbidden_name = name)
    
    # 가격이 0 이하 체크
    if price <= 0:
        raise ZeroPriceException(item_name = name)
    
    # 정상 등록
    item_id = len(fake_items) + 1
    fake_items[item_id] = {"name" : name, "price" : price}
    return {'message' : 'Item이 생성되었습니다', 'item_id' : item_id}