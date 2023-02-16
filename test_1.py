import aiohttp
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a bot instance and get its token from environment variables
bot = Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
dp = Dispatcher(bot)

# Define a handler function for /start command
@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    await message.reply("Hello! Welcome to my bot.")

# Define a handler function for /help command
@dp.message_handler(commands=['help'])
async def help_command_handler(message: types.Message):
    help_text = "This is a simple Telegram bot. Available commands:\n/start - start the bot\n/help - show this help message\n"
    await message.reply(help_text, parse_mode=ParseMode.MARKDOWN)

# Define a handler function for text messages
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(f"You said: {message.text}")

# Start the bot
async def main():
    await bot.send_message(chat_id='<your chat id>', text='Bot started')
    await executor.start_polling(dp, skip_updates=True)

asyncio.run(main())
