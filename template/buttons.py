import nextcord
import nextcord.ext


class ButtonUrl(nextcord.ui.View):
    def __init__(self, name: str, url: str):
        super().__init__()
        self.name = name
        self.url = url
        self.timeout = 60

        self.url_button = nextcord.ui.Button(label=self.name, style=nextcord.ButtonStyle.url, url=self.url)
        self.add_item(self.url_button)
