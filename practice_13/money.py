from abc import abstractmethod


class Expression:
    pass


class Money(Expression):
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    # TODO: nullとの等価性比較
    # TODO: 他のオブジェクトとの等価性比較
    def equals(self, object: "Money"):
        money = object
        return self._amount == money._amount and self._currency == money._currency

    def currency(self):
        return self._currency

    def plus(self, added: "Money"):
        return Money(self._amount + added._amount, self._currency)

    def to_string(self):
        return f"{self._amount} {self._currency}"

    @abstractmethod
    def times(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")


class Bank:
    @staticmethod
    def reduce(source: Expression, to: str):
        return Money.dollar(10)


# TODO: hashCode()
class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)
