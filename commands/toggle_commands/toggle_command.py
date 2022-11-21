import nextcord
import nextcord.ext
from nextcord.ext import commands, application_checks
from database import database_connect


class ToggleCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_database = database_connect.DatabaseConnect(
            pool_name="toggle_command",
            pool_size=2
        )

    @nextcord.slash_command(
        name="nyro-toggle-command",
        description="Toggle a command on and off",
        force_global=True
    )
    @application_checks.has_permissions(administrator=True)
    async def toggle_command(self, ctx: nextcord.Interaction, command: str):
        guild_id = ctx.guild.id

        connection = self.connection_database.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        sql_command = f"SELECT {command} FROM commands WHERE serverID=%s"
        sql_data = [int(guild_id)]

        cursor.execute(sql_command, sql_data)
        result_data = cursor.fetchall()

        if int(result_data[0][0]) != 1:
            sql_command = f"UPDATE commands SET {command}=true WHERE serverID=%s"
            sql_data = [int(guild_id)]

            cursor.execute(sql_command, sql_data)
            connection.commit()
            connection.close()
            await ctx.send(f"The command {command} is now active.", ephemeral=True)
            return

        sql_command = f"UPDATE commands SET {command}=false WHERE serverID=%s"
        sql_data = [int(guild_id)]

        cursor.execute(sql_command, sql_data)
        connection.commit()
        connection.close()
        await ctx.send(f"The command {command} is now inactive.", ephemeral=True)


def setup(bot):
    bot.add_cog(ToggleCommand(bot))
