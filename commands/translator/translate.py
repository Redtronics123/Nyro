import nextcord.ext
from nextcord.ext import commands
from deep_translator import GoogleTranslator
from template import string_select


class Translate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-translate",
        description="Translate any text to any language",
        force_global=True
    )
    async def translate(self, ctx: nextcord.Interaction, text: str):
        translator_view = string_select.TemplateStringSelect(
            ctx,
            ["German", "English", "Danish", "Finnish", "French", "Indonesian", "Irish", "Italian", "Latin"],
            placeholder="Select a language"
        )
        await ctx.send(view=translator_view, ephemeral=True)
        await translator_view.wait()

        try:
            translator = GoogleTranslator(target=str(translator_view.select.values[0]).lower())
        except IndexError:
            return await ctx.send("No language selected.", ephemeral=True)

        translated_text = translator.translate(text=text)

        await ctx.send(translated_text, ephemeral=True)


def setup(bot):
    bot.add_cog(Translate(bot))
