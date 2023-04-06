"""Draws a tarot card. """
import hikari
import lightbulb
import random

from cogs.embedStyles import palette


tarot_draw = lightbulb.Plugin("cogs.tarot")


@tarot_draw.command()
@lightbulb.command("tarot", "Draws a tarot card!")
@lightbulb.implements(lightbulb.SlashCommand)
async def tarot(ctx: lightbulb.Context) -> None:
    """Draws a tarot card."""
    cards = [
        "The Fool",
        "The Magician",
        "The High Priestess",
        "The Empress",
        "The Emperor",
        "The Hierophant",
        "The Lovers",
        "The Chariot",
        "Strength",
        "The Hermit",
        "Wheel of Fortune",
        "Justice",
        "The Hanged Man",
        "Death",
        "Temperance",
        "The Devil",
        "The Tower",
        "The Star",
        "The Moon",
        "The Sun",
        "Judgement",
        "The World",
        "Ace of Wands",
        "Two of Wands",
        "Three of Wands",
        "Four of Wands",
        "Five of Wands",
        "Six of Wands",
        "Seven of Wands",
        "Eight of Wands",
        "Nine of Wands",
        "Ten of Wands",
        "Page of Wands",
        "Knight of Wands",
        "Queen of Wands",
        "King of Wands",
        "Ace of Pentacles",
        "Two of Pentacles",
        "Three of Pentacles",
        "Four of Pentacles",
        "Five of Pentacles",
        "Six of Pentacles",
        "Seven of Pentacles",
        "Eight of Pentacles",
        "Nine of Pentacles",
        "Ten of Pentacles",
        "Page of Pentacles",
        "Knight of Pentacles",
        "Queen of Pentacles",
        "King of Pentacles",
        "Ace of Cups",
        "Two of Cups",
        "Three of Cups",
        "Four of Cups",
        "Five of Cups",
        "Six of Cups",
        "Seven of Cups",
        "Eight of Cups",
        "Nine of Cups",
        "Ten of Cups",
        "Page of Cups",
        "Knight of Cups",
        "Queen of Cups",
        "King of Cups",
        "Ace of Swords",
        "Two of Swords",
        "Three of Swords",
        "Four of Swords",
        "Five of Swords",
        "Six of Swords",
        "Seven of Swords",
        "Eight of Swords",
        "Nine of Swords",
        "Ten of Swords",
        "Page of Swords",
        "Knight of Swords",
        "Queen of Swords",
        "King of Swords",
    ]
    draw = random.choice(cards)
    embed = hikari.Embed(
        title="Drawing A Tarot Card! 🌒",
        description=f"{ctx.member.mention} drew a tarot card and got **{draw}**!",
        colour=random.choice(palette),
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    if draw == "The Fool":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg"
        )
    elif draw == "The Magician":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg"
        )
    elif draw == "The High Priestess":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/8/88/RWS_Tarot_02_High_Priestess.jpg"
        )
    elif draw == "The Empress":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/d/d2/RWS_Tarot_03_Empress.jpg"
        )
    elif draw == "The Emperor":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg"
        )
    elif draw == "The Hierophant":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/8/8d/RWS_Tarot_05_Hierophant.jpg"
        )
    elif draw == "The Lovers":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/3/3a/TheLovers.jpg"
        )
    elif draw == "The Chariot":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/9/9b/RWS_Tarot_07_Chariot.jpg"
        )
    elif draw == "Strength":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/f/f5/RWS_Tarot_08_Strength.jpg"
        )
    elif draw == "The Hermit":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/4/4d/RWS_Tarot_09_Hermit.jpg"
        )
    elif draw == "Wheel of Fortune":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg"
        )
    elif draw == "Justice":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/e/e0/RWS_Tarot_11_Justice.jpg"
        )
    elif draw == "The Hanged Man":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/2/2b/RWS_Tarot_12_Hanged_Man.jpg"
        )
    elif draw == "Death":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/d/d7/RWS_Tarot_13_Death.jpg"
        )
    elif draw == "Temperance":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/RWS_Tarot_14_Temperance.jpg/150px-RWS_Tarot_14_Temperance.jpg"
        )
    elif draw == "The Devil":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/5/55/RWS_Tarot_15_Devil.jpg"
        )
    elif draw == "The Tower":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/5/53/RWS_Tarot_16_Tower.jpg"
        )
    elif draw == "The Star":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/d/db/RWS_Tarot_17_Star.jpg"
        )
    elif draw == "The Moon":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/7/7f/RWS_Tarot_18_Moon.jpg"
        )
    elif draw == "The Sun":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/1/17/RWS_Tarot_19_Sun.jpg"
        )
    elif draw == "Judgement":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/RWS_Tarot_20_Judgement.jpg/220px-RWS_Tarot_20_Judgement.jpg"
        )
    elif draw == "The World":
        embed.set_image(
            "https://upload.wikimedia.org/wikipedia/commons/f/ff/RWS_Tarot_21_World.jpg"
        )

    await ctx.respond(embed=embed)


def load(bot):
    bot.add_plugin(tarot_draw)


def unload(bot):
    bot.remove_plugin(tarot_draw)
