from money import Money


# TODO: $5 + 10 CHF = $10
# TODO: Moneyの丸目処理をどうするか？
def test_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10).equals(five.times(2))
    assert Money.dollar(15).equals(five.times(3))


def test_equality():
    assert Money.dollar(5).equals(Money.dollar(5))
    assert not Money.dollar(5).equals(Money.dollar(6))
    assert not Money.franc(5).equals(Money.dollar(5))


def test_currency():
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()
