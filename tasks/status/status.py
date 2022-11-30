import nextcord
import nextcord.ext
from nextcord.ext import commands, tasks
import asyncio


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @tasks.loop(seconds=30)
    async def status(self):
        await self.bot.change_presence(
            activity=nextcord.Game(f"Nyro supported {len(self.bot.guilds)} server"),
            status=nextcord.Status.do_not_disturb
        )
        await asyncio.sleep(10)
        await self.bot.change_presence(
            activity=nextcord.Game(f"Do you need help? | /nyro-help"),
            status=nextcord.Status.do_not_disturb
        )
        await asyncio.sleep(10)
        await self.bot.change_presence(
            activity=nextcord.Game("Natural language processing"),
            status=nextcord.Status.do_not_disturb
        )

    @commands.Cog.listener()
    async def on_ready(self):
        self.status.start()
        print("loops started")


def setup(bot):
    bot.add_cog(Status(bot))
