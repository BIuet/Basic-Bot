import discord
from discord.ext import commands
from datetime import datetime as d
import random
import aiohttp
import asyncio

class Search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def cats(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("http://thecatapi.com/api/images/get?format=src") as resp:
                if resp.status != 200:
                    ctx.send("Oh no! I couldn't find any cats!")
                else:
                    try:
                        data = resp.url

                        await ctx.send(data)
                    except Exception:
                        await ctx.send("Oh no! The cats are on fire!")
                        
    @commands.command(aliases=['ud'])
    async def urban(self, ctx, *, arg):
        search = arg.replace(" ","+")
        url = "http://api.urbandictionary.com/v0/define?term={}".format(search)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                result = await r.json(content_type= None)
                if result["list"]:
                    definition = result['list'][0]['definition']
                    example = result['list'][0]['example']
                    defs = len(result['list'])
                    embed = discord.Embed(title='Top Definition', description=definition)
                    embed.set_author(name=arg, icon_url='https://i.imgur.com/bLf4CYz.png')
                    embed.add_field(name="Example:", value=example, inline=False)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Your search terms gave no results.")
        
def setup(bot):
    bot.add_cog(Search(bot))
