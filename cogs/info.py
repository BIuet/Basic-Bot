import discord
from discord.ext import commands
import datetime
from datetime import datetime as d
import asyncio

class Info(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['server','info'], no_pm=True)
    @commands.guild_only()
    async def serverinfo(self, ctx):
        '''See information about the server.'''
        server = ctx.guild
        total_users = len(server.members)
        online = len([m for m in server.members if m.status != discord.Status.offline])
        text_channels = len([x for x in server.channels if isinstance(x, discord.TextChannel)])
        voice_channels = len([x for x in server.channels if isinstance(x, discord.VoiceChannel)])
        categories = len(server.channels) - text_channels - voice_channels
        passed = (ctx.message.created_at - server.created_at).days
        created_at = "Since {}. That's over {} days ago!".format(server.created_at.strftime("%d %b %Y %H:%M"), passed)


        data = discord.Embed(description=created_at)
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Categories", value=categories)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner))
        data.set_footer(text="Server ID: " + str(server.id))
        data.set_author(name=server.name, icon_url=None or server.icon_url)
        data.set_thumbnail(url=None or server.icon_url)
        try:
            await ctx.send(embed=data)
        except discord.HTTPException:
            em_list = await embedtobox.etb(data)
            for page in em_list:
                await ctx.send(page)
                
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
        
    @commands.command(aliases=['del','clear'])
    @has_access()
    async def purge(self, ctx, limit : int):
        '''Clean a number of messages'''
        await ctx.message.channel.purge(limit=limit+1)
        
    @commands.Cog.listener()
    async def on_guild_join(guild):
        await guild.owner.send(f'Heya! Just to let you know, Photon Bot has been added to your discord server, {guild}!\nFeel free to type ``o help`` at any time to receive a commands help message!')
        
def setup(bot):
    bot.add_cog(Info(bot))
