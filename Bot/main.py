# == Discord Imports == #
import discord
from discord.ext import commands

# == Python Moduel Imports == #
import os
from pathlib import Path

# == Var Imports == #
from constants import Tokens


class Bot(commands.Bot):

    def __init__(self) -> None:
        intents = discord.Intents.all()

        super().__init__(command_prefix="?", intents=intents)

    def run(self) -> None:
        super().run(Tokens.BOT_TOKEN)

    async def on_ready(self):
        print("Logged in!")

bot = Bot()
bot.load_extension('exts.fun.fun')
bot.run()