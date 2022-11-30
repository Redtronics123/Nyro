import nextcord.ext
from nextcord.ext import commands
from database import database_connect


class CommandStatus(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_database = database_connect.DatabaseConnect(
            pool_name="check_command_status",
            pool_size=3
        )

    @commands.Cog.listener()
    async def on_guild_join(self, ctx: nextcord.Interaction):
        guild_id = ctx.guild.id

        connection = self.connection_database.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        sql_command = "INSERT INTO commands (ServerID) VALUE (%s)"
        sql_data = [int(guild_id)]

        cursor.execute(sql_command, sql_data)
        cursor.commit()
        connection.close()


def setup(bot):
    bot.add_cog(CommandStatus(bot))
