import nextcord
import nextcord.ext
from nextcord.ext import commands
from database import database_connect


class StatusCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_database = database_connect.DatabaseConnect(
            pool_name="toggle_command_status",
            pool_size=1
        )


def setup(bot):
    bot.add_cog(StatusCommand(bot))
