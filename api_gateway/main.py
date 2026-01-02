from fastapi import FastAPI, Request
from pydantic import BaseModel
from model_service.predict import predict
import time
import uuid
from monitoring.logger import logger

app = FastAPI()

class Input(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Sentiment API Running" }

@app.post("/predict")
def get_prediction(data: Input, request: Request):
    logger.info("REQUEST RECEIVED")
    start = time.time()
    request_id = str(uuid.uuid4())[:8]

    try:
        prediction = predict(data.text)
        latency = round((time.time() - start) * 1000, 2)

        logger.info(
            f"request_id={request_id} ip={request.client.host} "
            f"text=\"{data.text}\" prediction={prediction} latency_ms={latency}"
        )

        return {"sentiment": prediction, "latency_ms": latency}

    except Exception as e:
        logger.error(f"request_id={request_id} error={str(e)}")
        raise
