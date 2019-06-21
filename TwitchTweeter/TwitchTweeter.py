from redbot.core import commands


class TwitchTweeter(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def setupTweet(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("it WORK!!!! YE HA")
