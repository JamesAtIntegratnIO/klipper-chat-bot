from os import environ
from discord.ext import commands
from cogs.github_cog import GithubCog
from cogs.kevin import Kevin
from cogs.info import Information


if __name__ == '__main__':

    BOT = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                       description="Klipper Support Bot\nI'll PM you some helpful links if you ask nicely")
    BOT.add_cog(Kevin(BOT))
    BOT.add_cog(GithubCog(BOT))
    BOT.add_cog(Information(BOT))
    BOT.run(environ.get('DISCORDTOKEN'))
