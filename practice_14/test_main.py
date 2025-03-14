from money import Money, Bank, Expression, Sum


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


def test_simple_addition():
    five = Money.dollar(5)
    sum_expr = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(sum_expr, "USD")
    assert Money.dollar(10).equals(reduced)


def test_plus_returns_sum():
    five = Money.dollar(5)
    result = five.plus(five)
    sum_expr = result
    assert five.equals(sum_expr.augend)
    assert five.equals(sum_expr.addend)


def test_reduce_sum():
    sum_expr = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum_expr, "USD")
    assert Money.dollar(7).equals(result)


def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1).equals(result)


def test_reduce_money_different_currenry():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1).equals(result)
