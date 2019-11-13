import discord
from discord.ext import commands
from datetime import datetime as d
import os
import asyncio
import sqlite3

class Database(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    def connect():
      conn = sqlite3.connect("arras.db")
      c = conn.cursor()
      
    def close():
      conn.close()
    
    @commands.Cog.listener()
    async def on_guild_join(guild):
        connect()
        c.execute(f"CREATE TABLE IF NOT EXISTS users(user STR, tank STR, score INT)")
        await guild.owner.send(f'Heya! Thanks for being awesome and ')
        
    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        start = d.timestamp(d.now())

        msg = await ctx.send(content='Pinging')

        await msg.edit(content=f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.')
        return
        
def setup(bot):
    bot.add_cog(Database(bot))
