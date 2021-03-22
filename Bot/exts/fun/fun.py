import discord, asyncio, random, time, datetime
from discord.ext import commands
import re
import sys
from discord.ext.commands import clean_content

class TextConverters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
  
    @commands.command()
    async def drunkify(self, ctx, *, s):
        lst = [str.upper, str.lower]
        newText = await commands.clean_content().convert(ctx, ''.join(random.choice(lst)(c) for c in s))
        if len(newText) <= 150:
            await ctx.send(newText)
        else:
            try:
                await ctx.author.send(newText)
                error=discord.Embed(color=0xe83b3b)
                error.add_field(name="Error!", value="Your message in emojis exceeds 150 characters! \nSo I sent it to your dms!", inline=False)
                error.set_footer(text=f"This message will delete in 60 seconds!")
                await ctx.send(embed=error, delete_after=60)
            except discord.Forbidden as discorderror:
                error2=discord.Embed(color=0xe83b3b)
                error2.add_field(name="Error!", value=f"Discord throwed a error: {discorderror}", inline=False)
                error2.set_footer(text=f"This message will delete in 60 seconds!")
                await ctx.send(embed=error2, delete_after=60)
            except Exception:
                error3=discord.Embed(color=0xe83b3b)
                error3.add_field(name="Error!", value="Looks like something you inputted was not allowed! \nMaybe retry...", inline=False)
                error3.set_footer(text=f"This message will delete in 60 seconds!")
                await ctx.send(embed=error3, delete_after=60)

    @commands.command()
    async def emojify(self, ctx, *, text: str):
        await ctx.message.delete()
        emojified = ''
        formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
        if text == '':
            error=discord.Embed(color=0xe83b3b)
            error.add_field(name="Error!", value="Looks like you inputted nothing! \nMaybe retry...", inline=False)
            error.set_footer(text=f"This message will delete in 60 seconds!")
            await ctx.send(embed=error, delete_after=60)
        else:
            for i in formatted:
                if i == ' ':
                    emojified += '     '
                else:
                    emojified += ':regional_indicator_{}: '.format(i)
            if len(emojified) + 2 >= 150:
                error2=discord.Embed(color=0xe83b3b)
                error2.add_field(name="Error!", value="Your message evened the 150-character limit!", inline=False)
                error2.set_footer(text=f"This message will delete in 60 seconds!")
                await ctx.send(embed=error2, delete_after=60)
            if len(emojified) <= 25:
                error3=discord.Embed(color=0xe83b3b)
                error3.add_field(name="Error!", value="Looks like something you inputted was not allowed! \nMaybe retry...", inline=False)
                error3.set_footer(text=f"This message will delete in 60 seconds!")
                await ctx.send(embed=error3, delete_after=60)
            else:
                await ctx.send(''+emojified+'')

def setup(bot):
    bot.add_cog(TextConverters(bot))