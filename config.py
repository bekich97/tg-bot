import logging
import os
from dotenv import load_dotenv
import telebot

# To load variables from .env
load_dotenv()

# Create bot and pass it your bot's token.
bot = telebot.TeleBot(os.getenv('API_TOKEN'), parse_mode="HTML")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )
logger = logging.getLogger(__name__)