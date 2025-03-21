import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging
import random
import time
from prometheus_fastapi_instrumentator import Instrumentator


class Text(BaseModel):
    term: str
    intent: str

app = FastAPI()

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Instrumentation for Prometheus
instrumentor = Instrumentator()
instrumentor.instrument(app).expose(app)

@app.get("/")
def root():
    return {"message": "FastAPI with Docker Compose"}

@app.get("/random")
def get_random():
    return {"random_number": random.randint(1, 100)}

@app.get("/delay")
def delayed_response():
    time.sleep(2)  # Simulate slow response
    return {"message": "Delayed response"}

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response

@app.post("api/v1/query")
async def test_query(request: Request):
    logger.info(f"Request: {request.method} {request.url}")
    return {"message": "Success"}

@app.post("/text/")
async def create_item(text: Text):
    print(text)
    return {
        'status': 'success',
        'status_code': 200,
        'term': text.term,
        'intent': text.intent
    }


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8888)
