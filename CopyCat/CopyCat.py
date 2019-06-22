from redbot.core import commands


class CopyCat(commands.Cog):
    """" Copys what th user inputs"""

    @commands.command()
    async def mimic(self, ctx, *, words):
        """Monkey Do"""
        await ctx.send(words)


