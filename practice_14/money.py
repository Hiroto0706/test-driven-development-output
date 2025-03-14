from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def reduce(bank: 'Bank', self, to: str) -> 'Money':
        pass


class Money(Expression):
    def __init__(self, amount: int, currency_code: str):
        self._amount = amount
        self._currency = currency_code

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: 'Money') -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        rate = bank.rate(self.currency, to)
        return Money(self._amount / rate, to)

    def currency(self) -> str:
        return self._currency

    def equals(self, obj) -> bool:
        if not isinstance(obj, Money):
            return False
        return self._amount == obj._amount and self.currency() == obj.currency()

    def __str__(self) -> str:
        return f"{self._amount} {self._currency}"

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, "CHF")


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: 'Bank',  to: str) -> Money:
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, from_c: str, to_c: str, rate: int):
        pass

    def rate(self, from_c: str, to_c: str):
        return 2 if from_c == 'CHF' and to_c == 'USD' else 1


class Pair:
    def __init__(self, from_c: str, to_c: str):
        self._from = from_c
        self._to = to_c

    def equals(self, obj) -> bool:
        pair = obj
        return self._from == pair._from and self._to == pair._to

    def hash_code() -> int:
        return 0
