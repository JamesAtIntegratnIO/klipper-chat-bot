import github
from os import environ

from discord.ext import commands


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