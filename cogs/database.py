import discord
from discord.ext import commands
from datetime import datetime as d
import os
import asyncio
import sqlite3

class Database(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        c.execute(f"CREATE TABLE IF NOT EXISTS users(user STR, score INT)")
        
    def connect():
      conn = sqlite3.connect("photon.db")
      c = conn.cursor()
      
    def close():
      conn.close()
        
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
