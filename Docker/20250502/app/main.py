from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import Base, engine, SessionLocal, User


# DB 테이블 생성 (서버 시작 시 1회)
Base.metadata.create_all(bind = engine)

app = FastAPI()

# 요청마다 DB 세션 열기
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users")
def create_user(name : str, age : int, db : Session = Depends(get_db)):
    new_user = User(name = name, age = age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id" : new_user.id, "name" : new_user.name, "age" : new_user.age}

@app.get("/users")
def list_users(db : Session = Depends(get_db)):
    users = db.query(User).all()
    return users

