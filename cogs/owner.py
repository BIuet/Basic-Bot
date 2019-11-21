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
        if ctx.channel.name == 'photon-bot':
            await ctx.message.delete()
            message = await ctx.send('**How to add messages to priority list:**\n1. Type in ``o add`` and the name of the suggestor in a mention.')
            await message.pin()
            message = await ctx.send('Priority List:\n')
            await message.pin()
        else:
            await ctx.send("This channel isn't named ``photon-bot``.")
            
    @commands.command(aliases=['halp'])
    async def shelp(self, ctx):
        embed = discord.Embed(title='Photon Help', description='List of Suggestion Commands')
        data.add_field(name="purge <number>", value='Clears a specific number of messages from the channel!')
        data.add_field(name="setup", value="Only used to set up ``photon-bot`` channel. Use once unless you want to break it xD")
        data.add_field(name="add <id>", value="Adds a suggestion in ``photon-bot`` to the pins. Only workable in ``photon-bot`` channel.")
        data.add_field(name="poll <question>", value="Creates a simple yes/no poll and sends it to ``photon-bot`` channel.")
        data.add_field(name="suggest <suggestion>",value="Creates a suggestion. Limited to one per person. You can edit it by using this command.")
        
    @commands.command()
    async def poll(self, ctx, sleep: int, *,arg):
        embed = discord.Embed(title=arg,description='Poll created by '+ctx.message.author)
        channel = discord.utils.get(ctx.message.guild.text_channels, name='photon-bot')
        message = await channel.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🌀')
        await message.add_reaction('❓')
        
    @commands.command()
    async def add(self, ctx, member: discord.member.mention,)
        await ctx.message.delete()
        messages = await channel.history().flatten()
        message=messages[0]
        
        
        
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.owner.send(f'Heya! Just to let you know, Photon Bot has been added to your discord server, {guild}!\nFeel free to type ``o help`` at any time to receive a commands help message!\nIf you want a suggestions function, follow the instructions below:\n\n1. Create a read-only channel named ``photon-bot``\n2. Add the *member* Photon and give Photon access, and grant ALL message-related permissions (so Photon will function well). This includes add reactions and pinning stuff. \n4. Type in ``o setup`` in that channel and wait.\n5. Have fun! Now anyone can suggest stuff and access ``o shelp``!')
        
def setup(bot):
    bot.add_cog(Owner(bot))
