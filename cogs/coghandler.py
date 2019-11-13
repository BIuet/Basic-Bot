import discord
from discord.ext import commands
from datetime import datetime as d
import random

class Cog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["reload"])
    async def reloadcog(self, ctx, *, cog: str):
        """ Reload any cog """
        cog = f"cogs.{cog}"
        message = await ctx.send(f"Preparing to reload {cog}...")
        try:
            ctx.bot.reload_extension(cog)
            await message.edit(content='Cog was reloaded successfully!')
        except commands.ExtensionError:
            await message.edit(content='Error reloading cog.')
        
def setup(bot):
    bot.add_cog(Cog(bot))