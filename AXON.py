from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/chat")
def chat(data: dict):
    
    user_message = data["message"]