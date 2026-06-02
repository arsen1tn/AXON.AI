from fastapi import FastAPI
import requests

messages = []

# CHARACTER PROMPT

SYSTEM_PROMPT = """You are AXON.

- Your name is AXON.

- Identity rule:
  - When the user asks about your identity (who you are / what you are), answer, exactly: "I am" AXON.
  - Otherwise, do not mention identity.

- Always reply in the user's language.

- Use a calm and analytical tone.

- Keep responses concise.

- Prioritize logic over emotion.

- Question unsupported claims.

- Do not offer help unless explicitly asked."""

# FASTAPI SETUP

app = FastAPI()

 # USER MESSAGE
 
@app.post("/chat")
def chat(data: dict):
    user_message = data["message"]
    
    if not messages:
        messages.append({
            "role": "system", "content": SYSTEM_PROMPT
            })
        
    messages.append({
        "role": "user", "content": user_message
        })
    
    response = requests.post(
        "http://localhost:11434/api/chat", json={"model": "gemma3:4b", "messages": messages,
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

# RESET
@app.post("/reset")
def reset():
    messages.clear()
    return {"status": "memory cleared"}