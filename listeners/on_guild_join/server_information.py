import nextcord
import nextcord.ext
from nextcord.ext import commands
from database import database_connect
import datetime


class ServerInformation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connect_database = database_connect.DatabaseConnect(
            pool_name="Information",
            pool_size=3
        )

    @commands.Cog.listener()
    async def on_guild_join(self, ctx: nextcord.Interaction):
        guild_id = ctx.guild.id
        date = datetime.date.today()

        connection = self.connect_database.connection_pool.get_connection(prepared=True)
        cursor = connection.cursor()

        sql_command = "INSERT INTO discordServer (ServerID, ServerName, Date) VALUES (%s, %s, %s)"
        sql_data = (int(guild_id), str(ctx), str(date))

        cursor.execute(sql_command, sql_data)
        connection.commit()
        connection.close()
        

def setup(bot):
    bot.add_cog(ServerInformation(bot))
