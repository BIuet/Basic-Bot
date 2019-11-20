import discord
from discord.ext import commands
from datetime import datetime as d
import random

class Cog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    def has_access():
        def predicate(ctx):
            return ctx.message.author.id == 625354389061894145
        return commands.check(predicate)
        
    @commands.command()
    @has_access(
    async def reload(self, ctx, *, cog: str):
        """ Reload any cog """
        cog = f"cogs.{cog}"
        message = await ctx.send(f"Preparing to reload {cog}...")
        try:
            ctx.bot.reload_extension(cog)
            await message.edit(content='Cog was reloaded successfully!')
        except commands.ExtensionError:
            await message.edit(content='Error reloading cog.')
    
    @commands.command()
    @has_access(
    async def unload(self, ctx, *, cog: str):
        cog = f"cogs.{cog}"
        message = await ctx.send(f"Preparing to remove {cog}...")
        try:
            ctx.bot.unload_extension(cog)
            await message.edit(content='Cog was unloaded successfully!')
        except commands.ExtensionError:
            await message.edit(content='Error removing cog.')

    @commands.command()
    @has_access(
    async def load(self, ctx, *, cog: str):
        cog = f"cogs.{cog}"
        message = await ctx.send(f"Preparing to load {cog}...")
        try:
            ctx.bot.load_extension(cog)
            await message.edit(content='Cog was loaded successfully!')
        except commands.ExtensionError:
            await message.edit(content='Error loading cog.')
        
def setup(bot):
    bot.add_cog(Cog(bot))
