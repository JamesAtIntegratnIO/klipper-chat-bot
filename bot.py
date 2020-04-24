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

    @commands.command()
    async def example(self, ctx, message):
        await ctx.send(self.get_response("example", message))

    @commands.command()
    async def docs(self, ctx, message):
        await ctx.send(self.get_response("docs", message))

    @commands.command()
    async def tutorials(self, ctx, message):
        await ctx.send(self.get_response("tutorials", message))

    @commands.command()
    async def macros(self, ctx, message):
        await ctx.send(self.get_response("macros", message))


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
                   description='Relatively simple music bot example')

bot.add_cog(Kevin(bot))
# bot.add_cog(GitBot(bot))
bot.run(environ.get('DISCORDTOKEN'))
