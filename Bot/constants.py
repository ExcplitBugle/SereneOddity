from os import getenv
from discord import Colour

from dotenv import load_dotenv

class Tokens:
    load_dotenv()

    BOT_TOKEN = getenv("BOT_TOKEN")
    #Adding DB INFO Later!
