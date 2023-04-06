"""Draws a card. """
import hikari
import lightbulb
import random

from cogs.embedStyles import palette


drawer = lightbulb.Plugin("cogs.draw")


@drawer.command()
@lightbulb.command("draw", "Draw a card!")
@lightbulb.implements(lightbulb.SlashCommand)
async def draw(ctx: lightbulb.Context) -> None:
    """Draws a card."""
    cards = [
        "Ace of Diamonds",
        "Two of Diamonds",
        "Three of Diamonds",
        "Four of Diamonds",
        "Five of Diamonds",
        "Six of Diamonds",
        "Seven of Diamonds",
        "Eight of Diamonds",
        "Nine of Diamonds",
        "Ten of Diamonds",
        "Jack of Diamonds",
        "Queen of Diamonds",
        "King of Diamonds",
        "Ace of Clubs",
        "Two of Clubs",
        "Three of Clubs",
        "Four of Clubs",
        "Five of Clubs",
        "Six of Clubs",
        "Seven of Clubs",
        "Eight of Clubs",
        "Nine of Clubs",
        "Ten of Clubs",
        "Jack of Clubs",
        "Queen of Clubs",
        "King of Clubs",
        "Ace of Hearts",
        "Two of Hearts",
        "Three of Hearts",
        "Four of Hearts",
        "Five of Hearts",
        "Six of Hearts",
        "Seven of Hearts",
        "Eight of Hearts",
        "Nine of Hearts",
        "Ten of Hearts",
        "Jack of Hearts",
        "Queen of Hearts",
        "King of Hearts",
        "Ace of Spades",
        "Two of Spades",
        "Three of Spades",
        "Four of Spades",
        "Five of Spades",
        "Six of Spades",
        "Seven of Spades",
        "Eight of Spades",
        "Nine of Spades",
        "Ten of Spades",
        "Jack of Spades",
        "Queen of Spades",
        "King of Spades",
    ]
    embed = hikari.Embed(
        title="Drawing A Card! 🃏",
        description=f"{ctx.member.mention} drew a card and got **{random.choice(cards)}**!",
        colour=random.choice(palette),
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    await ctx.respond(embed=embed)


def load(bot):
    bot.add_plugin(drawer)


def unload(bot):
    bot.remove_plugin(drawer)
