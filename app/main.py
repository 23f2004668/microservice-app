from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379, db=0)

@app.get("/")
def home():
    return {"message": "FastAPI service working!"}

@app.get("/ping-redis")
def ping_redis():
    try:
        r.set("test", "microservices-ok")
        value = r.get("test").decode()
        return {"redis_status": "connected", "value": value}
    except Exception as e:
        return {"redis_status": "failed", "error": str(e)}
