from redbot.core import commands


class Twitchw``Tweeter(commands.Cog):
    """Posts a Tweet when streamers go live"""

    @commands.command()
    async def setupTweet(self, ctx):
        """Used to set up and change the bots setting"""
        # Your code will go here
        await ctx.send("Hello world")
