# TODO: hashCode()
class Dollar:
    def __init__(self, amount: int):
        # TODO: amountをプライベートにする
        self.amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

    # TODO: nullとの等価性比較
    # TODO: 他のオブジェクトとの等価性比較
    def equals(self, object: "Dollar"):
        dollar = object
        return self.amount == dollar.amount
