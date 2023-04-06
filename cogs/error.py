"""Errors. """


class Error:
    """Returns errors."""

    def __init__(self) -> None:
        pass

    def tooManyDiceError():
        return "You've rolled too many dice! Please try the command again, entering a number less than 1001 in *Amount*. "

    def notEnoughDiceError():
        return "You can't roll less than 1 die! Please try the command again, entering a number between 1 and 1000 in the *Amount* field. "

    def notAnIntError():
        return "You entered something other than a number in the *Amount*, *d*, or modifier fields (*Add*, *Subtract*, *Multiply*, *Divide*). Please try again, entering only numbers in all fields. "

    def divideByZeroError():
        return "You can't divide by zero. Please choose a different number to divide your roll by. "

    def tooManySides():
        return "You can't roll dice with more than 1000 sides! Please try again, entering a number of sides between 1 and 1000 in the *d* field. "

    def notEnoughSides():
        return "You can't roll dice with fewer than 2 sides! Please try again, entering a number of sides between 1 and 1000 in the *d* field. "
