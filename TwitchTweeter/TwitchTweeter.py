from redbot.core import commands


class TwitchTweeter(commands.Cog):
    """Posts a Tweet when streamers go live"""

    @commands.command()
    async def setupTweet(self, ctx):
        """Used to set up and change the bots setting """
        # Your code will go here
        await ctx.send("Hello world")

    @commands.command()
    async def addStream(self, ctx, nickName, twitchID):
        """ Add a new streamer to the list"""

        await ctx.send("The TwitchID "+twitchID+"has been added. The Nickname is: "+nickName)