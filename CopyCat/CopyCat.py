from redbot.core import commands


class CopyCat(commands.Cog):
    """" Copys what the user inputs"""

    @commands.command()
    async def mimic(self, ctx, *, words):
        """Monkey Do"""
        await ctx.send(words+"Sam is the best" )

      #  await ctx.send("I can do stuff!")


