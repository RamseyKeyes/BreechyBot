from redbot.core import commands


class CopyCat(commands.Cog):
    """" Copys what the user inputs"""

    @commands.command()
    async def mimic(self, ctx):
        """Monkey Do"""
        await ctx.send(" It's a Girl")

      #  await ctx.send("I can do stuff!")


