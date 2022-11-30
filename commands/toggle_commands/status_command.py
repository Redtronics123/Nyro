import nextcord
from nextcord.ext import commands
from database import database_connect


class StatusCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_database = database_connect.DatabaseConnect(
            pool_name="toggle_command_status",
            pool_size=1
        )

    @nextcord.slash_command(
        name="nyro-toggle-command-status",
        description="Check the status of a command",
        force_global=True
    )
    async def toggle_command_status(self, ctx: nextcord.Interaction, command: str):
        guild_id = ctx.guild.id

        connection = self.connection_database.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        sql_command = f"SELECT {command.lower()} FROM commands WHERE serverID=%s"
        sql_data = [int(guild_id)]

        cursor.execute(sql_command, sql_data)
        result_data = cursor.fetchall()
        connection.close()

        if result_data[0][0] != 1:
            await ctx.send(f"The Command {command} is inactive.")
            return
        await ctx.send(f"The Command {command} is active.")


def setup(bot):
    bot.add_cog(StatusCommand(bot))
