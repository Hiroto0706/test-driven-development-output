from abc import abstractmethod


class Money:
    def __init__(self, amount: int):
        self._amount = amount

    # TODO: nullとの等価性比較
    # TODO: 他のオブジェクトとの等価性比較
    def equals(self, object: "Money"):
        if self.__class__ != object.__class__:
            return False

        money = object
        return self._amount == money._amount

    @abstractmethod
    def times(multiplier: int):
        pass

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount)

    @staticmethod
    def franc(amount: int):
        return Franc(amount)


# TODO: hashCode()
class Dollar(Money):
    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)


# TODO: dollar と francの重複
# TODO: timesの一般化
class Franc(Money):
    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)
