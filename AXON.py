from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/chat")
