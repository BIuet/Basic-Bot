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
        c.execute(f"CREATE TABLE IF NOT EXISTS users(user STR, coins INT)")
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
    async def view(self, ctx, *, member : discord.member):
        embed = discord.Embed()
        embed.colour = member.role.colour
        embed.set_author(name=member, icon_url=member.avatar_url)
        connect()
        embed.add_field(name='Balance',value=retrieve(member,coins))
        ctx.send(embed=embed)
        close()
        
    @commands.command(name='award',aliases=['a','gift','give'])
    @is_owner()
    async def award(self, ctx, *, member : discord.member):
        embed = discord.Embed()
        embed.colour = member.role.colour
        embed.set_author(name=member, icon_url=member.avatar_url)
        connect()
        amount = random.randint(20,60)
        currentbalance = retrieve(member,coins)
        if currentbalance == '':
            c.execute("INSERT INTO users VALUES(?,0)",(member,))
            conn.commit()
        amount = int(amount)
        currentbalance = currentbalance+amount
        c.execute("UPDATE users SET coins = ? WHERE user =?",(currentbalance,member,))
        conn.commit()
        embed.add_field(name='Yay!',value='This user got awarded {} coins!'(amount))
        ctx.send(embed=embed)
        close()
        
def setup(bot):
    bot.add_cog(Database(bot))
