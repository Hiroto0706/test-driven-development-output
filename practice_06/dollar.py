from money import Money


# TODO: hashCode()
class Dollar(Money):
    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)
