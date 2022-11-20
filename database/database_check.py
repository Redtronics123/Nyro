import mysql.connector
from mysql.connector.errors import Error
import json


class DatabaseCheck:
    def __init__(self):
        with open("/home/nils/PycharmProjects/nyro/config.json", "r") as conf:
            config = json.load(conf)
            self.host = config["mariadb"]["host"]
            self.user = config["mariadb"]["user"]
            self.password = config["mariadb"]["password"]
            self.database = config["mariadb"]["database"]

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

    def create_database(self):
        print("hi")
