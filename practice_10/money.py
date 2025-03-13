from abc import abstractmethod


class Money:
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    # TODO: nullとの等価性比較
    # TODO: 他のオブジェクトとの等価性比較
    def equals(self, object: "Money"):
        if self.__class__ != object.__class__:
            return False

        money = object
        return self._amount == money._amount

    def currency(self):
        return self._currency

    @abstractmethod
    def times(self, multiplier: int):
        pass

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Franc(amount, "CHF")


# TODO: hashCode()
class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int):
        return Money.dollar(self._amount * multiplier)


# TODO: dollar と francの重複
# TODO: timesの一般化
class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int):
        return Money.franc(self._amount * multiplier)
