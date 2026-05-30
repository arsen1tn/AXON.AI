from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import asyncio
import requests
# TOKEN

TOKEN = "nigg"

bot = Bot(token=TOKEN)

dp = Dispatcher()

# MESSAGE HANDLER

@dp.message(Command("start"))
async def start_handler(message):
    await message.answer("Supp, I'm AXON. What do you want to do today?")

@dp.message()
async def message_handler(message):
    
    user_message = message.text
    
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={ "message": user_message},
    )
    
    data = response.json()
    
    ai_response = data["response"]
    
    await message.answer(ai_response)
# START 
async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)

asyncio.run(main())