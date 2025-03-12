from money import Money


# TODO: dollar と francの重複
# TODO: timesの一般化
class Franc(Money):
    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)
