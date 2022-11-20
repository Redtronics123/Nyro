import nextcord.ext
from nextcord.ext import commands
import datetime


class TemplateEmbed(nextcord.Embed):
    def __init__(self, bot: commands.Bot, ctx: nextcord.Interaction, color: nextcord.Color):
        super().__init__()

        self.color = color
        self.bot = bot
        self.ctx = ctx
        self.title = self.bot.user.name
        self.description = "This message was created automatically."

        self.set_author(name=self.ctx.user.name, icon_url=self.ctx.user.avatar)
        self.set_footer(text=f"Created automatically by {self.bot.user.name} | {datetime.date.today()}")
        self.set_thumbnail(url=self.bot.user.avatar)
