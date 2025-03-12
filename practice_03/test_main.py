from money import Dollar


# TODO: $5 + 10 CHF = $10
# TODO: Moneyの丸目処理をどうするか？
def test_multiplication():
    five = Dollar(5)
    ten = five.times(2)
    assert ten.amount == 10

    fifteen = five.times(3)
    assert fifteen.amount == 15


def test_equality():
    assert Dollar(5).equals(Dollar(5))
