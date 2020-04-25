from os import environ
from discord.ext import commands
import yaml


class Kevin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.command_list = self._get_command_list()

    @staticmethod
    def _get_command_list():
        with open('command_list.yaml') as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def _get_options(self, parent_command):
        option_list = []
        for key in self.command_list.get(parent_command):
            option_list.append(key)
        return option_list

    def _get_response(self, parent_command, child_command):
        return self.command_list.get(parent_command).get(child_command)

    async def _help_option_wrapper(self, ctx):
        msg = ctx.message.content
        option = msg[len(ctx.prefix) + len(ctx.invoked_with) + 1:]
        if option == '':
            await ctx.send(f"```{ctx.invoked_with} options:\n" +
                           "\n".join(self._get_options(ctx.invoked_with)) + "```")
        else:
            await ctx.send(self._get_response(ctx.invoked_with, option))

    @commands.command(aliases=['e'], help='!e option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def example(self, ctx):
        await self._help_option_wrapper(ctx)

    @commands.command(aliases=['d'], help='!d option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def docs(self, ctx):
        await self._help_option_wrapper(ctx)

    @commands.command(aliases=['t'], help='!t option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def tutorials(self, ctx):
        await self._help_option_wrapper(ctx)

    @commands.command(aliases=['m'], help='!m option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def macros(self, ctx):
        await self._help_option_wrapper(ctx)


bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Klipper Support Bot')
bot.add_cog(Kevin(bot))
# bot.add_cog(GitBot(bot))
bot.run(environ.get('DISCORDTOKEN'))
