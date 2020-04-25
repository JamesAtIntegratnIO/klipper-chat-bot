from os import environ
from discord.ext import commands
import github
from datetime import datetime, timedelta, timezone


class GithubCog(commands.Cog):
    def __init__(self, bot):
        self.g_hub = github.Github(environ.get('GITHUBKEY'))
        self.bot = bot
        self.repo = self.get_repo()

    def get_repo(self):
        return self.g_hub.get_repo("KevinOConnor/klipper")

    @commands.command(help='!list_open_issues NumberOfDays')
    @commands.has_any_role("Admin", "Helper")
    async def list_open_issues(self, ctx):
        msg = ctx.message.content
        option = msg[len(ctx.prefix) + len(ctx.invoked_with) + 1:]
        try:
            option = int(option)
        except ValueError:
            await ctx.send("Did not receive number. Providing 1 day")
            option = 1
        if option > 3:
            await ctx.send("I'm not fetching more than 3 days")
        else:
            open_issues = self.repo.get_issues(state='open')
            wanted_open_issues = []
            message = ''
            for issue in open_issues:
                time_since_created = datetime.now() - issue.created_at
                if time_since_created < timedelta(days=option):
                    wanted_open_issues.append(issue)
            for issue in wanted_open_issues:
                await ctx.send(f'Title: **{issue.title}**\nCreated: {issue.created_at}\nLink: {issue.url}\n\n')
