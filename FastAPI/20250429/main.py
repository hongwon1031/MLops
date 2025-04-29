from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# 물품 데이터
fake_products = {
    1 : {'name' : '가위', 'price' : 1000},
    2 : {'name' : '과자', 'price' : 1500},
    3 : {'name' : '모자', 'price' : 7000}
}

# 상품 입력 모델
class Product(BaseModel):
    name : str
    price : int

# 상품 응답 모델
class ProductOut(BaseModel):
    name : str
    price : int

# 가격이 0 이하일 때 발생하는 예외
class ZeroPriceException(Exception):
    def __init__(self, product_name: str):
        self.product_name = product_name

# 금지된 이름일 때 발생하는 예외
class ForbiddenNameException(Exception):
    def __init__(self, forbidden_name: str):
        self.forbidden_name = forbidden_name


@app.exception_handler(ZeroPriceException)
async def zero_price_exception_handler(request: Request, exc: ZeroPriceException):
    return JSONResponse(
        status_code=400,
        content={"detail": f"'{exc.product_name}'의 가격이 0 이하입니다! 올바른 가격을 입력하세요."}
    )

@app.exception_handler(ForbiddenNameException)
async def forbidden_name_exception_handler(request: Request, exc: ForbiddenNameException):
    return JSONResponse(
        status_code=403,
        content={"detail": f"'{exc.forbidden_name}'은 금지된 이름입니다."}
    )

    
# 상품 등록 (POST)
@app.post("/products/", response_model=ProductOut)
def create_product(product: Product):
    if product.name.lower() == "admin":
        raise ForbiddenNameException(forbidden_name=product.name)

    if product.price <= 0:
        raise ZeroPriceException(product_name=product.name)

    product_id = len(fake_products) + 1
    fake_products[product_id] = {"name": product.name, "price": product.price}
    return product

# 상품 조회 (GET)
@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int):
    product = fake_products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

