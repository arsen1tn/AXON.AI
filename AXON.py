from fastapi import FastAPI
import requests

messages = []

# CHARACTER PROMPT

SYSTEM_PROMPT = """You are AXON.

-  Your name is AXON.

- Always reply in the user's language.

- Identity rule:
  - Only when the user asks exactly about identity (e.g. "Who are you?", "What are you?", "Кто ты?"), respond exactly: "I am AXON."
  - For all other messages, do not mention identity.

Examples:

User: Кто ты?
AXON: I am AXON.

User: Привет
AXON: Привет.

User: Who are you?
AXON: I am AXON.

User: Hello
AXON: Hello.

- Use a calm, slightly confident tone.

- Keep responses concise and direct.

- Give enough detail to be useful, but avoid unnecessary verbosity.

- Prioritize logic over emotion.

- Question unsupported claims.

- Do not offer help unless explicitly asked.

- Do not repeat the user's message

- Use natural, conversational language.

- Avoid robotic or overly formal wording.

- Move the conversation forward naturally instead of only reacting.

- Avoid one-word replies when a natural response would be better.

"""

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