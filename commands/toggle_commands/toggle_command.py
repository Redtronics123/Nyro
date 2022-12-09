import nextcord.ext
from nextcord.ext import commands, application_checks
from database import database_connect
import os
from template import string_select


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
    async def toggle_command(self, ctx: nextcord.Interaction):
        guild_id = ctx.guild.id
        registed_commands = []
        command = None

        connection = self.connection_database.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        for directory in os.listdir("../nyro/commands"):
            if directory != "toggle_commands":
                registed_commands.append(directory)

        toggle_view = string_select.TemplateStringSelect(
            label_name=registed_commands,
            placeholder="Select a command"
        )
        await ctx.send(view=toggle_view, ephemeral=True)
        await toggle_view.wait()
        command = toggle_view.select.values[0]

        sql_command = f"SELECT {command.lower()} FROM commands WHERE serverID=%s"
        sql_data = [int(guild_id)]

        cursor.execute(sql_command, sql_data)
        result_data = cursor.fetchall()

        if int(result_data[0][0]) != 1:
            sql_command = f"UPDATE commands SET {command.lower()}=true WHERE serverID=%s"
            sql_data = [int(guild_id)]

            cursor.execute(sql_command, sql_data)
            connection.commit()
            connection.close()
            await ctx.send(f"The command {command} is now active.", ephemeral=True)
            return

        sql_command = f"UPDATE commands SET {command.lower()}=false WHERE serverID=%s"
        sql_data = [int(guild_id)]

        cursor.execute(sql_command, sql_data)
        connection.commit()
        connection.close()
        await ctx.send(f"The command {command} is now inactive.", ephemeral=True)


def setup(bot):
    bot.add_cog(ToggleCommand(bot))
