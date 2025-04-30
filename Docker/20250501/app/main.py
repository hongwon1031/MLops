from fastapi import FastAPI
import redis
import time

app = FastAPI()
time.sleep(3)

r = redis.Redis(host = 'redis', port = 6379, decode_responses = True)

@app.get('/')
def read_root():
    return {"message": "Hello from FastAPI + Redis"}

@app.get("/set")
def set_key():
    r.set("mykey", "hello")
    return {"status" : "ok"}

@app.get("/get")
def get_key():
    value = r.get("mykey")
    return {"value" : value}