# TODO: equals()
# TODO: hashCode()
class Dollar:
    def __init__(self, amount: int):
        # TODO: amountをプライベートにする
        self.amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

    @staticmethod
    def equals(object):
        return True
