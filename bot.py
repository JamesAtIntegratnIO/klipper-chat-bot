import yaml
import github
from os import environ

from discord.ext import commands


class Kevin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.command_list = self.get_command_list()

    @staticmethod
    def get_command_list():
        with open('command_list.yaml') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def get_response(self, parent_command, child_command):
        return self.command_list.get(parent_command).get(child_command)

    def get_options(self, parent_command):
        option_list = []
        for key in self.command_list.get(parent_command):
            option_list.append(key)
        return option_list

    @commands.command(aliases=['e'], help='!e option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def example(self, ctx):
        # Next we get the message with the command in it.
        msg = ctx.message.content

        # Extracting the text sent by the user
        # ctx.invoked_with gives the alias used
        # ctx.prefix gives the prefix used while invoking the command
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used)+1 + len(alias_used):]
        print(text)
        if text == '':
            await ctx.send(f"Example Options:\n" + "\n".join(self.get_options("example")))
        else:
            await ctx.send(self.get_response("example", text))

    @commands.command(aliases=['d'], help='!d option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def docs(self, ctx):
        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used)+1 + len(alias_used):]
        if text == '':
            await ctx.send(f"Docs Options:\n" + "\n".join(self.get_options("docs")))
        else:

            await ctx.send(self.get_response("docs", text))

    @commands.command(aliases=['t'], help='!t option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def tutorials(self, ctx):
        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used)+1 + len(alias_used):]
        if text == '':
            await ctx.send(f"Tutorials Options:\n" + "\n".join(self.get_options("tutorials")))
        else:
            await ctx.send(self.get_response("tutorials", text))

    @commands.command(aliases=['m'], help='!m option\nWithout an option will list options')
    @commands.has_permissions(embed_links=True)
    async def macros(self, ctx):

        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used)+1 + len(alias_used):]
        if text == '':
            await ctx.send(f"Macro Options:\n" + "\n".join(self.get_options("macros")))
        else:
            await ctx.send(self.get_response("macros", text))


class GitBot(commands.Cog):
    def __init__(self, bot):
        self.g = github.Github(environ.get('GITHUBKEY'))
        self.bot = bot
        self.repo = self.get_repo()

    def get_repo(self):
        return self.g.get_repo("KevinOConnor/klipper")

    @commands.command()
    async def list_open_issues(self, ctx):
        open_issues = self.repo.get_issues(state='open')
        for issue in open_issues:
            await ctx.send(issue)


bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Klipper Support Bot')
bot.add_cog(Kevin(bot))
# bot.add_cog(GitBot(bot))
bot.run(environ.get('DISCORDTOKEN'))
