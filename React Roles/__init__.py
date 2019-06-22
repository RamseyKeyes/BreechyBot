from .react_roles import ReactRoles


def setup(bot):
    # Creating the cog
    c = ReactRoles(bot)
    # Finally, add the cog to the bot.
    bot.add_cog(c)