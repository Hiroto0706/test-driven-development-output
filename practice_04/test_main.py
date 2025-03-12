from money import Dollar


# TODO: $5 + 10 CHF = $10
# TODO: 5CHF * 2 = 10CHF
# TODO: Moneyの丸目処理をどうするか？
def test_multiplication():
    five = Dollar(5)
    assert Dollar(10).equals(five.times(2))
    assert Dollar(15).equals(five.times(3))


def test_equality():
    assert Dollar(5).equals(Dollar(5))
    assert not Dollar(5).equals(Dollar(6))
