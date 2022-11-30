import nextcord
import wikipedia
from algorithm import string_split
from template import embeds
from nextcord.ext import commands


class Search:
    def __init__(self, ctx: nextcord.Interaction, bot: commands.Bot, text: list):
        self.text = text
        self.result = None
        self.bot = bot
        self.ctx = ctx

    async def search(self):
        ai_embed = embeds.TemplateEmbed(self.bot, self.ctx, nextcord.Color.dark_gold())

        for res in self.text:
            try:
                self.result: str = wikipedia.summary(res)
            except wikipedia.WikipediaException:
                continue

            if len(self.result) > 1024:
                string_splitted = string_split.StringSplit(self.result).string_splitting()

                for element in string_splitted:
                    ai_embed.add_field(name=str(res) + "-->", value=str(element), inline=False)

            else:
                ai_embed.add_field(name=str(res) + "-->", value=str(res), inline=False)

        await self.ctx.send(embed=ai_embed, ephemeral=True)
