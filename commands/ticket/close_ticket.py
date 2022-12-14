import nextcord
import nextcord.ext
from nextcord.ext import commands, application_checks
from database import database_check


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
        if await database_check.DatabaseCheck().check_command_status(ctx, "ticket"):
            return

        category = nextcord.utils.get(ctx.guild.categories, name="ticket")
        if len(category.channels) == 0:
            return await ctx.send("There are no tickets.", ephemeral=True)

        for channel in category.channels:
            if channel.name == ticket.name:
                await ticket.delete()
                return await ctx.send("Ticket was deleted successful.")

        await ctx.send("This channel is not in the category **ticket**.", ephemeral=True)


def setup(bot):
    bot.add_cog(TicketClose(bot))
