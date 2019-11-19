import discord
from discord.ext import commands
from datetime import datetime as d
import random

class Cog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @is_owner()
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
    @is_owner()
    async def unload(self, ctx, *, cog: str):
        cog = f"cogs.{cog}"
        message = await ctx.send(f"Preparing to remove {cog}...")
        try:
            ctx.bot.unload_extension(cog)
            await message.edit(content='Cog was unloaded successfully!')
        except commands.ExtensionError:
            await message.edit(content='Error removing cog.')

    @commands.command()
    @is_owner()
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
