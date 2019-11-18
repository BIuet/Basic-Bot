import discord
from discord.ext import commands
import datetime
from datetime import datetime as d
import asyncio

class Owner(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    def has_access():
        def predicate(ctx):
            return ctx.message.author.id == 625354389061894145 or ctx.message.author == ctx.message.guild.owner
        return commands.check(predicate)
        
    @commands.command(aliases=['set-up'])
    @has_access()
    async def setup(self, ctx):
        await ctx.message.channel.purge(limit=limit+1)
        
        
        
    def setup(bot):
    bot.add_cog(Info(bot))
