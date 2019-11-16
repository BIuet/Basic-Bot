import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix = 'o ', case_insensitive=True)

cogs = ['cogs.database','cogs.coghandler',]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    for cog in cogs:
        bot.load_extension(cog)
    print(bot.cogs)
    await bot.change_presence(activity=discord.Game(name='type --help for commamds!', type=0))
    return
    
bot.run('NjQ0NzE2MTU3Njg5MDA0MDg0.Xc4sfQ.UkWVomtzQUy-3BaBh120vP7qPf0', bot=True, reconnect=True)
