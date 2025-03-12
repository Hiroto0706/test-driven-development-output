# TODO: dollar と francの重複
# TODO: equals()の一般化
# TODO: timesの一般化
class Franc:
    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)

    def equals(self, object: "Franc"):
        franc = object
        return self._amount == franc._amount
