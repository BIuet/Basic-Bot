import discord
from discord.ext import commands
import random

class Utility(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["setgame","game"])
    async def change(self, ctx, *, arg):
        await self.bot.change_presence(activity=discord.Game(name=arg, type=0))
        await ctx.send('Game presence changed!')
        
    @commands.command()
    async def quote(self, ctx, id: int, channel: discord.TextChannel=None):
        await ctx.message.delete()
        msg = await ctx.fetch_message(id)
        if not msg:
            return await ctx.send('Could not find that message!', delete_after=3.0)
        em = discord.Embed(color=0x00FFFF, description=msg.clean_content, timestamp=msg.created_at)
        em.set_author(name=str(msg.author), icon_url=msg.author.avatar_url)
        if isinstance(msg.channel, discord.TextChannel):
            em.set_footer(text='#' + str(msg.channel))
        else:
            em.set_footer(text=str(msg.channel))
        await ctx.send(embed=em)
        
    @commands.command()
    async def choose(self, ctx, *, choices: commands.clean_content):
        '''Choose between multiple choices. Use `,` to seperate choices.'''
        choices = choices.split(',')
        if len(choices) < 2:
            return await ctx.send('Not enough choices to pick from.')
        choices[0] = ' ' + choices[0]
        await ctx.send(str(random.choice(choices))[1:])
        
def setup(bot):
    bot.add_cog(Utility(bot))
