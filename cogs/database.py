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
      
    def close(self):
        conn.close()
    
    def retrieve(self,user):
        self.c.execute("SELECT won FROM users WHERE user = ?", (user,))
        retrieved = self.c.fetchall()
        retrieved = str(retrieved)
        retrieved = retrieved[2:-3]
        return retrieved
        
    @commands.command(
        name='view',
        aliases=['v','profile','balance']
    )
    async def view(self, ctx, *, member : discord.member=None):
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        embed = discord.Embed()
        embed.colour = user.role.colour
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.add_field(name='Rock Paper Scissors Games Won',value=self.retrieve(user))
        ctx.send(embed=embed)
        
    @commands.command(
        name='check',
    )
    async def check(self, ctx):
        currentbalance = self.retrieve(ctx.message.author)
        if currentbalance == '':
            self.c.execute("INSERT INTO users VALUES(?,0)",(ctx.message.author,))
            self.conn.commit()
            print("Added f'{ctx.message.author} to database")
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        currentbalance = retrieve(member,won)
        if currentbalance == '':
            self.c.execute("INSERT INTO currency VALUES(?,0,0)",(membername,))
            self.conn.commit()
            print("Added f'{member} to database")
        
def setup(bot):
    bot.add_cog(Database(bot))
