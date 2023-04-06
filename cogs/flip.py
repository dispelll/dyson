"""Flips a coin. """
import hikari
import lightbulb
import random

from cogs.embedStyles import palette


flipper = lightbulb.Plugin("cogs.flip")


@flipper.command()
@lightbulb.command("flip", "Flip a coin!")
@lightbulb.implements(lightbulb.SlashCommand)
async def flip(ctx: lightbulb.Context) -> None:
    """Flips a coin."""
    flip = ["Heads", "Tails"]
    embed = hikari.Embed(
        title="Flipping A Coin! 🪙",
        description=f"{ctx.member.mention} flipped a coin and got **{random.choice(flip)}**!",
        colour=random.choice(palette),
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    await ctx.respond(embed=embed)


def load(bot):
    bot.add_plugin(flipper)


def unload(bot):
    bot.remove_plugin(flipper)
