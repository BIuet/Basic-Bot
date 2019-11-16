import discord
from discord.ext import commands
from datetime import datetime as d
import os
import asyncio
import random
import sqlite3

class Database(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        conn = sqlite3.connect("photon.db")
        c = conn.cursor()
        c.execute(f"CREATE TABLE IF NOT EXISTS users(user STR, won INT)")
        conn.close()
        
    def connect():
        conn = sqlite3.connect("photon.db")
        c = conn.cursor()
      
    def close():
        conn.close()
    
    def retrieve(user, item):
        c.execute("SELECT ? FROM users WHERE user = ?", (item,user,))
        retrieved = c.fetchall()
        retrieved = str(retrieved)
        retrieved = retrieved[2:-3]
        return retrieved
        
    @commands.command(
        name='view',
        aliases=['v','profile','balance']
    )
    async def view(self, ctx, *, member : discord.member-None):
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        embed = discord.Embed()
        embed.colour = member.role.colour
        embed.set_author(name=member, icon_url=member.avatar_url)
        connect()
        embed.add_field(name='Rock Paper Scissors Games Won',value=retrieve(member,won))
        ctx.send(embed=embed)
        close()
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        connect()
        currentbalance = retrieve(member,won)
        if currentbalance == '':
            c.execute("INSERT INTO currency VALUES(?,0,0)",(membername,))
            conn.commit()
            print("Added f'{member} to database")
        close()
        
def setup(bot):
    bot.add_cog(Database(bot))
