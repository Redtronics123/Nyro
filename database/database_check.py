import mysql.connector
import nextcord
from mysql.connector.errors import Error
from database import database_connect
import json


class DatabaseCheck:
    def __init__(self):
        with open("/home/nils/PycharmProjects/nyro/config.json", "r") as conf:
            config = json.load(conf)
            self.host = config["mariadb"]["host"]
            self.user = config["mariadb"]["user"]
            self.password = config["mariadb"]["password"]
            self.database = config["mariadb"]["database"]

            self.connection_database = database_connect.DatabaseConnect(
                pool_name="check_command_status",
                pool_size=5
            )

    def check_for_connection(self):
        try:
            mysql.connector.connect(host=self.host, user=self.user, password=self.password)
            return True

        except Error:
            print("Database offline or you have a false config")
            exit()

    def check_configuration(self):
        connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        cursor = connection.cursor(prepared=True)

        sql_command = "show databases"
        cursor.execute(sql_command)

        for databases in cursor:
            if str(databases[0]).lower() == "nyro":
                return True

    async def check_command_status(self, ctx: nextcord.Interaction, command: str):
        guild_id = ctx.guild.id

        connection = self.connection_database.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        sql_command = f"SELECT {command} FROM commands WHERE serverID=%s"
        sql_data = [int(guild_id)]

        cursor.execute(sql_command, sql_data)
        result_data = cursor.fetchall()
        connection.close()

        if result_data[0][0] != 1:
            await ctx.send("Command is not enabled on this Server.")
            return True

    def create_database(self):
        print("Muss noch gemacht werden, wenn Datenbank steht.")
