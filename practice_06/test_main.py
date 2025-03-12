from dollar import Dollar
from franc import Franc


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
    assert Franc(5).equals(Franc(5))
    assert not Franc(5).equals(Franc(6))


def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10).equals(five.times(2))
    assert Franc(15).equals(five.times(3))
