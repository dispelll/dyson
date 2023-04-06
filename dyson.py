"""Runs the bot."""
import hikari
import lightbulb
import miru
import random

from cogs.embedStyles import ephemeral, palette
from cogs.roll import randTitle


bot = lightbulb.BotApp(
    token="TOKEN",
    intents=hikari.Intents.ALL,
    help_slash_command=None,
)
bot.load_extensions(
    "cogs.draw",
    "cogs.flip",
    "cogs.roll",
    "cogs.tarot",
)
miru.install(bot)


class RollButtons(miru.View):
    """Roll buttons."""

    def __init__(self):
        super().__init__(timeout=None)

    @miru.button(label="D4", custom_id="d4", style=hikari.ButtonStyle.SECONDARY)
    async def d4(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        """Roll a D4."""
        embed = hikari.Embed(
            title=f"{random.choice(randTitle)}",
            description=f"{ctx.member.mention}, you rolled a **d4** and got: `{random.randint(1,4)}`. ",
            colour=random.choice(palette),
        )
        embed.set_author(
            icon=ctx.member.display_avatar_url, name=ctx.member.display_name
        )
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="D6", custom_id="d6", style=hikari.ButtonStyle.SECONDARY)
    async def d6(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        """Roll a D6."""
        embed = hikari.Embed(
            title=f"{random.choice(randTitle)}",
            description=f"{ctx.member.mention}, you rolled a **d6** and got: `{random.randint(1,6)}`. ",
            colour=random.choice(palette),
        )
        embed.set_author(
            icon=ctx.member.display_avatar_url, name=ctx.member.display_name
        )
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="D8", custom_id="d8", style=hikari.ButtonStyle.SECONDARY)
    async def d8(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        """Roll a D8."""
        embed = hikari.Embed(
            title=f"{random.choice(randTitle)}",
            description=f"{ctx.member.mention}, you rolled a **d8** and got: `{random.randint(1,8)}`. ",
            colour=random.choice(palette),
        )
        embed.set_author(
            icon=ctx.member.display_avatar_url, name=ctx.member.display_name
        )
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="D10", custom_id="d10", style=hikari.ButtonStyle.SECONDARY)
    async def d10(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        """Roll a D10."""
        embed = hikari.Embed(
            title=f"{random.choice(randTitle)}",
            description=f"{ctx.member.mention}, you rolled a **d10** and got: `{random.randint(1,10)}`. ",
            colour=random.choice(palette),
        )
        embed.set_author(
            icon=ctx.member.display_avatar_url, name=ctx.member.display_name
        )
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="D12", custom_id="d12", style=hikari.ButtonStyle.SECONDARY)
    async def d12(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        """Roll a D12."""
        embed = hikari.Embed(
            title=f"{random.choice(randTitle)}",
            description=f"{ctx.member.mention}, you rolled a **d12** and got: `{random.randint(1,12)}`. ",
            colour=random.choice(palette),
        )
        embed.set_author(
            icon=ctx.member.display_avatar_url, name=ctx.member.display_name
        )
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="D20", custom_id="d20", style=hikari.ButtonStyle.SECONDARY)
    async def d20(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        """Roll a D20."""
        embed = hikari.Embed(
            title=f"{random.choice(randTitle)}",
            description=f"{ctx.member.mention}, you rolled a **d20** and got: `{random.randint(1,20)}`. ",
            colour=random.choice(palette),
        )
        embed.set_author(
            icon=ctx.member.display_avatar_url, name=ctx.member.display_name
        )
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="D100", custom_id="d100", style=hikari.ButtonStyle.SECONDARY)
    async def d100(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        """Roll a D100."""
        embed = hikari.Embed(
            title=f"{random.choice(randTitle)}",
            description=f"{ctx.member.mention}, you rolled a **d100** and got: `{random.randint(1,100)}`. ",
            colour=random.choice(palette),
        )
        embed.set_author(
            icon=ctx.member.display_avatar_url, name=ctx.member.display_name
        )
        await ctx.respond(embed=embed, flags=ephemeral)


@bot.listen()
async def start_views(event: hikari.StartedEvent) -> None:
    """Starts the button view."""
    view = RollButtons()
    await view.start()


@bot.command()
@lightbulb.command("dyson", "Tells you how to roll dice with Dyson! ")
@lightbulb.implements(lightbulb.SlashCommand)
async def dyson(ctx: lightbulb.Context) -> None:
    """Dyson help command."""
    help = hikari.Embed(
        title="Roll Dice With Dyson! 🎲",
        description="Use `/roll` to roll dice with Dyson! `/roll` starts with 2 fields: *Amount*, and *d*. In *Amount* put the number of dice you wish to roll. In *d* put the number of sides your dice should have (e.g. 4 for a d4, 6 for a d6, 42 for a d42, etc. ). Dyson can roll up to 1000 dice, with up to 1000 sides. \n\nYou can also use the *Add*, *Subtract*, *Multiply*, and *Divide* optional fields to modify rolls you make with Dyson. ",
        colour=random.choice(palette),
    )
    help.add_field(
        name="Flip A Coin! 🪙", value="Use `/flip` to flip a coin!", inline=False
    )
    help.add_field(
        name="Draw A Card! 🃏", value="Use `/draw` to draw a card!", inline=False
    )
    help.add_field(
        name="Draw A Tarot Card! 🌒",
        value="Use `/tarot` to draw a tarot card!",
        inline=False,
    )
    help.set_footer(text="Use the buttons below to roll some common polyhedral dice!")
    help.set_author(icon=ctx.member.display_avatar_url, name=ctx.member.display_name)
    await ctx.respond(embed=help, components=RollButtons())


bot.run(
    status=hikari.Status.IDLE,
    activity=hikari.Activity(
        name="the dice roll | /dyson", type=hikari.ActivityType.WATCHING
    ),
)
