"""Rolls dice! """
import hikari
import lightbulb
import random

from cogs.error import Error
from cogs.embedStyles import ephemeral, palette


roller = lightbulb.Plugin("cogs.roll")
randTitle = [
    "Throwing math rocks... 🎲",
    "Rolling dice... 🎲",
    "Checking for Yahtzee... 🎲",
    "Trying to ignore 1s... 🎲",
    "Rolling loaded dice... 🎲",
    "Predicting your bleak future... 🎲",
]


class Roll:
    """Rolls dice."""

    def __init__(self) -> None:
        pass

    def roll(end, amount):
        """Rolls dice within a range."""
        roll = [random.randint(1, int(end)) for i in range(int(amount))]
        return roll


@roller.command()
@lightbulb.option("divide", "A number to divide the roll by. ", required=False)
@lightbulb.option("multiply", "A number to multiply the roll by. ", required=False)
@lightbulb.option("subtract", "A number to subtract from the roll. ", required=False)
@lightbulb.option("add", "A number to add to the roll. ", required=False)
@lightbulb.option(
    "d", "The amount of sides your dice has (4 for d4, 6 for d6, etc. ). "
)
@lightbulb.option("amount", "The number of dice you want to roll. ")
@lightbulb.command("roll", "Rolls dice! ")
@lightbulb.implements(lightbulb.SlashCommand)
async def roll(ctx: lightbulb.Context) -> None:
    """Roll dice."""
    add = ctx.options.add
    amount = ctx.options.amount
    d = ctx.options.d
    divide = ctx.options.divide
    multiply = ctx.options.multiply
    subtract = ctx.options.subtract

    try:
        # Error catch block, with the remaining ValueError caught in except below.
        # Checking for NoneType here before converting optionals to ints to avoid TypeError.
        if add:
            add = int(ctx.options.add)
        if divide:
            divide = int(ctx.options.divide)
        if multiply:
            multiply = int(ctx.options.multiply)
        if subtract:
            subtract = int(ctx.options.subtract)
        if int(amount) < 1:
            error = hikari.Embed(
                title="Error! 🚨",
                description=f"{Error.notEnoughDiceError()}",
                colour=random.choice(palette),
            )
            await ctx.respond(embed=error, flags=ephemeral)
            return
        if int(amount) > 1000:
            error = hikari.Embed(
                title="Error! 🚨",
                description=f"{Error.tooManyDiceError()}",
                colour=random.choice(palette),
            )
            error.set_image("https://media.tenor.com/4IpoNRfu_hsAAAAC/wait-error.gif")
            await ctx.respond(embed=error, flags=ephemeral)
            return
        if int(d) < 2:
            error = hikari.Embed(
                title="Error! 🚨",
                description=f"{Error.notEnoughSides()}",
                colour=random.choice(palette),
            )
            error.set_image("https://media.tenor.com/4IpoNRfu_hsAAAAC/wait-error.gif")
            await ctx.respond(embed=error, flags=ephemeral)
            return
        if int(d) > 1000:
            error = hikari.Embed(
                title="Error! 🚨",
                description=f"{Error.tooManySides()}",
                colour=random.choice(palette),
            )
            error.set_image("https://media.tenor.com/4IpoNRfu_hsAAAAC/wait-error.gif")
            await ctx.respond(embed=error, flags=ephemeral)
            return
        if divide == "0":
            error = hikari.Embed(
                title="Error! 🚨",
                description=f"{Error.divideByZeroError()}",
                colour=random.choice(palette),
            )
            error.set_image("https://media.tenor.com/4IpoNRfu_hsAAAAC/wait-error.gif")
            await ctx.respond(embed=error, flags=ephemeral)
            return
        # Start actually rolling dice here.
        # Single roll.
        if amount == "1" and not add and not subtract and not divide and not multiply:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            singleRoll = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got a `{joinedRoll}`. ",
                colour=random.choice(palette),
            )
            singleRoll.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=singleRoll)
        # Flat roll.
        if amount != "1" and not add and not subtract and not multiply and not divide:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            flatRoll = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}` for a total of: `{summedRoll}`. ",
                colour=random.choice(palette),
            )
            flatRoll.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=flatRoll)
        # Just add.
        if add and not subtract and not multiply and not divide:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            addedRoll = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then added `{add}` for a total of: `{summedRoll + add}`. ",
                colour=random.choice(palette),
            )
            addedRoll.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=addedRoll)
        # Just multiply.
        if multiply and not add and not subtract and not divide:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            multipliedRoll = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then multiplied by `{multiply}` for a total of: `{summedRoll * multiply}`. ",
                colour=random.choice(palette),
            )
            multipliedRoll.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=multipliedRoll)
        # Just subtract.
        if subtract and not add and not multiply and not divide:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            subtractedRoll = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then subtracted `{subtract}` for a total of: `{summedRoll - subtract}`. ",
                colour=random.choice(palette),
            )
            subtractedRoll.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=subtractedRoll)
        # Just divide.
        if divide and not add and not multiply and not subtract:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            dividedRoll = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then divided by `{divide}` for a total of: `{summedRoll / divide}`. ",
                colour=random.choice(palette),
            )
            dividedRoll.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=dividedRoll)
        # Add then subtract.
        if add and subtract and not multiply and not divide:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            addThenSubtract = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then added `{add}` and subtracted `{subtract}` for a total of: `{summedRoll + add - subtract}`. ",
                colour=random.choice(palette),
            )
            addThenSubtract.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=addThenSubtract)
        # Multiply then add.
        if add and multiply and not subtract and not divide:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            multiplyThenAdd = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then multiplied by `{multiply}`, and added `{add}` for a total of: `{summedRoll * multiply + add}`. ",
                colour=random.choice(palette),
            )
            multiplyThenAdd.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=multiplyThenAdd)
        # Divide then add.
        if add and divide and not multiply and not subtract:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            divideThenAdd = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then divided by `{divide}`, and added `{add}` for a total of: `{summedRoll / divide + add}`. ",
                colour=random.choice(palette),
            )
            divideThenAdd.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=divideThenAdd)
        # Multiply then subtract.
        if subtract and multiply and not add and not divide:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            multiplyThenSubtract = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then multiplied by `{multiply}`, and subtracted by `{subtract}` for a total of: `{summedRoll * multiply - subtract}`. ",
                colour=random.choice(palette),
            )
            multiplyThenSubtract.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=multiplyThenSubtract)
        # Divide then subtract.
        if subtract and divide and not multiply and not add:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            divideThenSubtract = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then divided by `{divide}`, and subtracted `{subtract}` for a total of: `{summedRoll / divide - subtract}`. ",
                colour=random.choice(palette),
            )
            divideThenSubtract.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=divideThenSubtract)
        # Multiply then divide.
        if multiply and divide and not add and not subtract:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            multiplyThenDivide = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then multiplied by `{multiply}`, and divided by `{divide}` for a total of: `{summedRoll * multiply / divide}`. ",
                colour=random.choice(palette),
            )
            multiplyThenDivide.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=multiplyThenDivide)
        # All the marbles.
        if add and subtract and multiply and divide:
            roll = Roll.roll(end=d, amount=amount)
            joinedRoll = ",".join(str(i) for i in roll)
            summedRoll = sum(roll)
            allTheMarbles = hikari.Embed(
                title=f"{random.choice(randTitle)}",
                description=f"{ctx.member.mention}, you rolled **{amount}d{d}** and got `{joinedRoll}`, then multiplied by `{multiply}`, divided by `{divide}`, added `{add}`, and subtracted `{subtract}` for a total of: `{summedRoll * multiply / divide + add - subtract}`. ",
                colour=random.choice(palette),
            )
            allTheMarbles.set_author(
                icon=ctx.member.display_avatar_url, name=ctx.member.display_name
            )
            await ctx.respond(embed=allTheMarbles)

    except ValueError:
        error = hikari.Embed(
            title="Error! 🚨",
            description=f"{Error.notAnIntError()}",
            colour=random.choice(palette),
        )
        error.set_image("https://media.tenor.com/4IpoNRfu_hsAAAAC/wait-error.gif")
        await ctx.respond(embed=error, flags=ephemeral)
        return


def load(bot):
    bot.add_plugin(roller)


def unload(bot):
    bot.remove_plugin(roller)
