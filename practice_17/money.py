from abc import ABC, abstractmethod
from typing import Dict


class Expression(ABC):
    @abstractmethod
    def plus(added: 'Expression') -> 'Expression':
        pass

    @abstractmethod
    def reduce(bank: 'Bank', self, to: str) -> 'Money':
        pass

    @abstractmethod
    def times(multiplier: int) -> 'Money':
        pass


class Money(Expression):
    def __init__(self, amount: int, currency_code: str):
        self._amount = amount
        self._currency = currency_code

    def times(self, multiplier: int) -> 'Expression':
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: 'Expression') -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        rate = bank.rate(self._currency, to)
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
    def __init__(self, augend: 'Expression', addend: 'Expression'):
        self.augend = augend
        self.addend = addend

    def plus(self, added: Expression):
        return Sum(self, added)

    def reduce(self, bank: 'Bank',  to: str) -> "Money":
        amount = self.augend.reduce(
            bank, to)._amount + self.addend.reduce(bank, to)._amount
        return Money(amount, to)

    def times(self, multiplier: int):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))


class Bank:
    def __init__(self):
        self.rates: Dict[Pair, str] = {}

    def reduce(self, source: Expression, to: str) -> "Money":
        return source.reduce(self, to)

    def add_rate(self, from_c: str, to_c: str, rate: int):
        self.rates[Pair(from_c, to_c)] = rate

    def rate(self, from_c: str, to_c: str) -> int:
        if from_c == to_c:
            return 1
        return self.rates.get(Pair(from_c, to_c))


class Pair:
    def __init__(self, from_c: str, to_c: str):
        self._from = from_c
        self._to = to_c

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pair):
            return False
        return self._from == other._from and self._to == other._to

    def __hash__(self) -> int:
        return hash((self._from, self._to))
