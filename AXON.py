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

- Do not repeat the user's message.
   
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


#(venv) PS E:\Codes\MY PROJECTS\My_projects_main> python -m pip list
#Package            Version
#------------------ ---------
#aiofiles           25.1.0
#aiogram            3.28.2
#aiohappyeyeballs   2.6.2
#aiohttp            3.13.5
#aiosignal          1.4.0
#annotated-doc      0.0.4
#annotated-types    0.7.0
#anyio              4.13.0
#attrs              26.1.0
#certifi            2026.5.20
#charset-normalizer 3.4.7
#click              8.4.1
#colorama           0.4.6
#fastapi            0.136.3
#frozenlist         1.8.0
#h11                0.16.0
#idna               3.17
#magic-filter       1.0.12
#multidict          6.7.1
#pip                26.1.1
#propcache          0.5.2
#pydantic           2.13.4
#pydantic_core      2.46.4
#requests           2.34.2
#starlette          1.2.0
#typing_extensions  4.15.0
#typing-inspection  0.4.2
#urllib3            2.7.0
#uvicorn            0.48.0
#yarl               1.24.2