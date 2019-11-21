import traceback
import sys
from discord.ext import commands
import discord


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):
            return
        
        ignored = (commands.UserInputError)
        error = getattr(error, 'original', error)
        
        if isinstance(error, ignored):
            return
        
        elif isinstance(error, commands.CommandNotFound):
            return await ctx.send('That is an non-existent command! Try ``o help`` for a list of commands')

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
                return await ctx.send('You have inputted an invalid arguement. Please retry.')
            
        elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please specify an arguement.")
            
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
 
def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
