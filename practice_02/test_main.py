from money import Dollar


# TODO: $5 + 10 CHF = $10
# TODO: Moneyの丸目処理をどうするか？
def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert five.amount == 10
