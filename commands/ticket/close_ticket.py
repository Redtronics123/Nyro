import nextcord
import nextcord.ext
from nextcord.ext import commands, application_checks


class TicketClose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-ticket-close",
        description="Close ticket",
        force_global=True
    )
    @application_checks.has_permissions(administrator=True)
    async def ticket_close(self, ctx: nextcord.Interaction, ticket: nextcord.TextChannel):
        category = nextcord.utils.get(ctx.guild.categories, name="ticket")
        if len(category.channels) == 0:
            return await ctx.send("There are no tickets.", ephemeral=True)

        for channel in category.channels:
            if channel.name != ticket.name:
                return await ctx.send("This channel is not in the category **ticket**.", ephemeral=True)

        await ticket.delete()
        await ctx.send("Ticket was deleted successful.")


def setup(bot):
    bot.add_cog(TicketClose(bot))
