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
            await ctx.delete()
            message = await ctx.send('Priority List:\n')
            await message.pin()
        else:
            await ctx.send("This channel isn't named ``photon-bot``.")
            
    @commands.command(aliases=['halp'])
    @has_access()
    async def shelp(self, ctx):
        embed = discord.Embed(title='Photon Help', description='List of Commands only Owner can use')
        data.add_field(name="purge <number>", value='Clears a specific number of messages from the channel!')
        data.add_field(name="setup", value="Only used to set up ``photon-bot`` channel. Use once unless you want to break it xD")
        data.add_field(name="add <id>", value="Adds a suggestion in ``photon-bot`` to the pins. Only workable in ``photon-bot`` channel.")
        data.add_field(name="poll <question>", value="Creates a simple yes/no poll and sends it to ``photon-bot`` channel.")
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.owner.send(f'Heya! Just to let you know, Photon Bot has been added to your discord server, {guild}!\nFeel free to type ``o help`` at any time to receive a commands help message!\nIf you want a suggestions function, follow the instructions below:\n\n1. Create a read-only channel named ``photon-bot``\n2. Add the *member* Photon and give Photon access, and grant ALL message-related permissions (so Photon will function well). This includes add reactions and pinning stuff. \n4. Type in ``o setup`` in that channel and wait.\n5. Have fun! Now anyone can suggest stuff and access ``o shelp``!')
        
    def setup(bot):
    bot.add_cog(Info(bot))
