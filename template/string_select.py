import nextcord
import nextcord.ext


class TemplateStringSelect(nextcord.ui.View):
    def __init__(self, ctx: nextcord.Interaction, label_name: list, placeholder: str):
        super().__init__()
        self.ctx = ctx
        self.label_name = label_name
        self.options = []
        self.timeout = 60
        self.placeholder = placeholder

        for element in self.label_name:
            self.options.append(nextcord.SelectOption(label=str(element)))

        async def callback(interaction):
            self.stop()

        self.select = nextcord.ui.StringSelect(options=self.options, placeholder=self.placeholder)
        self.select.callback = callback

        self.add_item(self.select)
