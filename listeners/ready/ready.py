import nextcord
import nextcord.ext
from nextcord.ext import commands


class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot logged in as {self.bot.user}")
        print("""
            d8b   db db    db d8888b.  .d88b.  
            888o  88 `8b  d8' 88  `8D .8P  Y8. 
            88V8o 88  `8bd8'  88oobY' 88    88 
            88 V8o88    88    88`8b   88    88 
            88  V888    88    88 `88. `8b  d8' 
            VP   V8P    YP    88   YD  `Y88P'
        """)


def setup(bot):
    bot.add_cog(Ready(bot))
