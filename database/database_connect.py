from mysql.connector import pooling
import json


class DatabaseConnect:
    def __init__(self, pool_name: str, pool_size: int):
        with open("/home/nils/PycharmProjects/nyro/config.json", "r") as conf:
            config = json.load(conf)
            self.host = config["mariadb"]["host"]
            self.user = config["mariadb"]["user"]
            self.password = config["mariadb"]["password"]
            self.database = config["mariadb"]["database"]

        self.pool_name = pool_name
        self.pool_size = pool_size

        self.connection_pool = pooling.MySQLConnectionPool(
            pool_name=self.pool_name,
            pool_size=self.pool_size,
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            pool_reset_session=True
        )
