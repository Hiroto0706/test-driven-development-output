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
