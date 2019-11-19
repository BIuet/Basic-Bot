import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix = 'o ', case_insensitive=True)

cogs = ['cogs.commandhandler','cogs.coghandler','cogs.info','cogs.utils','cogs.owner']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    for cog in cogs:
        bot.load_extension(cog)
    print(bot.cogs)
    await bot.change_presence(activity=discord.Game(name='type "o help" for commamds!', type=0))
    return
    
bot.run('BOT TOKEN', bot=True, reconnect=True)
