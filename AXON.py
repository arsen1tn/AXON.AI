from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/chat")
def chat(data: dict):
    
    user_message = data["message"]
    response = requests.post(
        "http://localhost:11434/api/chat", json={"model": "qwen2.5:3b", "messages": [
            {
                "role": "user", "content": user_message
                }
            ]
                                                 }
        )
    
    result = response.json()
    
    ai_response = result["message"]["content"]
    
    return {
        "response": ai_response
        }
    