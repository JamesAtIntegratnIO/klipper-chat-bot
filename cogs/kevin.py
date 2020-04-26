from os import environ
from discord.ext import commands
import yaml
import difflib


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

    def _get_response(self, parent_command, option):
        response = self.command_list.get(parent_command).get(option)
        if not response:
            best_match = difflib.get_close_matches(option, self.command_list.get(parent_command))
            print(f'best_match: {best_match}')
            if not best_match:
                return f'Could not anything like option: {option}'
            else:
                return f'<{self.command_list.get(parent_command).get(best_match[0])}>'
        else:
            return f'<{response}>'

    async def _help_option_wrapper(self, ctx):
        msg = ctx.message.content
        option = msg[len(ctx.prefix) + len(ctx.invoked_with) + 1:]
        if option == '':
            await ctx.send(f"```{ctx.invoked_with} options:\n" +
                           "\n".join(self._get_options(ctx.invoked_with)) + "```")
        else:
            await ctx.send(self._get_response(ctx.invoked_with, option))

    @commands.command(help='!examples option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def examples(self, ctx):
        await self._help_option_wrapper(ctx)

    @commands.command(help='!docs option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def docs(self, ctx):
        await self._help_option_wrapper(ctx)

    @commands.command(help='!tutorials option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def tutorials(self, ctx):
        await self._help_option_wrapper(ctx)

    @commands.command(help='!macros option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def macros(self, ctx):
        await self._help_option_wrapper(ctx)

    @commands.command(help='!tools option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def tools(self, ctx):
        await self._help_option_wrapper(ctx)
