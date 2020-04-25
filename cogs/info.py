import discord, datetime, time
from discord.ext import commands

start_time = time.time()


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="get info about the bot")
    async def about(self, ctx):
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.title = "Klipper Chat Bot"
        embed.add_field(name="Author", value="BigD/Boboysdadda (same guy)", inline=False)
        embed.add_field(name="Contributors", value="Abom", inline=False)
        embed.add_field(name="Github", value="https://github.com/boboysdadda/klipper-chat-bot", inline=False)
        embed.set_footer(text="Built to Support Klipper - Brrt!!! Brrt!!!")
        message = "Name: klipper-chat-bot\n"
        message += "Author: BigD/Boboysdadda (same guy)\n"
        message += "Contributors: Abom\n"
        message += "Github: https://github.com/boboysdadda/klipper-chat-bot"
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(message)

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Built to Support Klipper - Brrt!!! Brrt!!!")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)
