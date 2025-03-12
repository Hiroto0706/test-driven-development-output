# TODO: Dollarの副作用をどうする？
class Dollar():
    def __init__(self, amount: int):
        # TODO: amountをプライベートにする
        self.amount = amount

    def times(self, multiplier: int):
        self.amount *= multiplier
