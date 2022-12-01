from nextcord.ext import commands
from database import database_check
import json
import os
import asyncio
from commands.music import music_nods


class Nyro(commands.Bot):
    def __init__(self):
        super().__init__()

    def main(self):
        with open("config.json", "r") as conf:
            config = json.load(conf)
            token = config["token"]
            prefix = config["prefix"]
            print("Config loaded")

        self.intents.all()
        self.remove_command("help")
        self.command_prefix = prefix
        print("Set Intents")

        database_check.DatabaseCheck().check_for_connection()
        print("Datenbank ready to connect")

        if not database_check.DatabaseCheck().check_configuration():
            database_check.DatabaseCheck().create_database()
            print("Created Database successful")
        print("Database is ready to use")

        for directory_commands in os.listdir("commands"):
            for file_commands in os.listdir(f"commands/{directory_commands}"):
                if file_commands.endswith(".py"):
                    self.load_extension(f"commands.{directory_commands}.{file_commands[:-3]}")

        for directory_listeners in os.listdir("listeners"):
            for file_listeners in os.listdir(f"listeners/{directory_listeners}"):
                if file_listeners.endswith(".py"):
                    self.load_extension(f"listeners.{directory_listeners}.{file_listeners[:-3]}")

        for directory_tasks in os.listdir("tasks"):
            for file_tasks in os.listdir(f"tasks/{directory_tasks}"):
                if file_tasks.endswith(".py"):
                    self.load_extension(f"tasks.{directory_tasks}.{file_tasks[:-3]}")
        print("Extensions loaded")

        self.run(token)


if __name__ == "__main__":
    Nyro().main()
