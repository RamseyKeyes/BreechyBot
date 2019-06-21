from .TwitchTweeter import TwitchTweeter


def setup(bot):
    bot.add_cog(TwitchTweeter())
