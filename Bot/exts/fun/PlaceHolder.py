import discord, asyncio, random, time, datetime
from discord.ext import commands
from discord.ext.commands import clean_content

class TextConverters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
  
    @commands.command(aliases=['mock'])
    async def drunkify(self, ctx, *, s):
        lst = [str.upper, str.lower]
        newText = await commands.clean_content().convert(ctx, ''.join(random.choice(lst)(c) for c in s))
        if len(newText) <= 380:
            await ctx.send(newText)
        else:
            try:
                await ctx.author.send(newText)
                await ctx.send(f"{ctx.author.mention} The output was very large so I sent It to your dms!")
            except Exception:
                await ctx.send(f"{ctx.author.mention} Seem's like there was a problem with your input!")
