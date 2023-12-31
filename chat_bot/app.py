import logging

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/favicon.ico")
def favicon():
    return FileResponse("static/favicon.ico", media_type="image/x-icon")


@app.get("/")
@app.get("/home")
def home():
    return "Hello World"


@app.post("/webhook")
async def webhook(request: Request):
    # Access request body using request object
    data = await request.json()
    logger.info(data)
    return {"fulfillmentText": "Hello from the bot world"}
