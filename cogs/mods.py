import discord
from discord.ext import commands

class Mods(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
                
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
                
    def has_access():
        def predicate(ctx):
            return ctx.message.author.id == 625354389061894145 or ctx.message.author == ctx.message.guild.owner
        return commands.check(predicate)
        
    @commands.command(aliases=['del','p','wipe','purge','clear'])
    @has_access()
    async def purge(self, ctx, limit : int, member:discord.Member=None):
        '''Clean a number of messages'''
        if member is None:
            await ctx.purge(limit=limit+1)
        else:
            async for message in ctx.channel.history(limit=limit+1):
                if message.author is member:
                    await message.delete()
        
    @commands.Cog.listener()
    async def on_guild_join(guild):
        await guild.owner.send(f'Heya! Just to let you know, Photon Bot has been added to your discord server, {guild}!\nFeel free to type ``o help`` at any time to receive a commands help message!')
                
        
def setup(bot):
    bot.add_cog(Mods(bot))
