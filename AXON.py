from fastapi import FastAPI
import requests

messages = []

app = FastAPI()

 # USER MESSAGE
 
@app.post("/chat")
def chat(data: dict):
    user_message = data["message"]
    messages.append({
        "role": "user", "content": user_message
        })
    
    response = requests.post(
        "http://localhost:11434/api/chat", json={"model": "qwen2.5:3b", "messages": messages,
            "stream": False
                                                 }
        )

# RESPONSE FROM AI MODEL
   
    result = response.json()
    
    ai_response = result["message"]["content"]
    
    messages.append({
        "role": "assistant", "content": ai_response
        })
    
    return {
        "response": ai_response
        }

