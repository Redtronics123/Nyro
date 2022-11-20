import nextcord
import nextcord.ext
from nextcord.ext import commands


class ToggleCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(ToggleCommand(bot))
