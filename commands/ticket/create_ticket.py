import nextcord
import nextcord.ext
from nextcord.ext import commands
from database import database_check


class TicketCreate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-ticket",
        description="Create a ticket",
        force_global=True
    )
    async def ticket_create(self, ctx: nextcord.Interaction):
        if await database_check.DatabaseCheck().check_command_status(ctx, "ticket"):
            return

        category = nextcord.utils.get(ctx.guild.categories, name="ticket")
        if category is None:
            category = await ctx.guild.create_category("ticket")

        if len(category.channels) == 50:
            return await ctx.send("There are to many tickets. Please try again later.", ephemeral=True)

        for channel in category.channels:
            if channel.name == f"ticket-{ctx.user.name.lower()}":
                return await ctx.send("You have an active ticket. Please use that.", ephemeral=True)

        ticket = await ctx.guild.create_text_channel(f"ticket-{ctx.user.name.lower()}", category=category)
        await ticket.set_permissions(ctx.guild.default_role, view_channel=False)
        await ticket.set_permissions(ctx.user, view_channel=True)

        await ticket.send(f"Hey {ctx.user.mention}, how can we help you?")
        await ctx.send("Your ticket was created successful.", ephemeral=True)


def setup(bot):
    bot.add_cog(TicketCreate(bot))
