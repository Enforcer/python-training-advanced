"""Implement appropriate dunder methods so operators are overloaded and tests pass."""
import unittest
from decimal import Decimal
from typing import Any, Self


class Money:
    def __init__(self, amount: Decimal, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other: "Money") -> Self:
        if not isinstance(other, Money):
            raise TypeError
        if other.currency != self.currency:
            raise ValueError("Cannot add Money of different currencies!")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: "Money") -> Self:
        if not isinstance(other, Money):
            raise TypeError
        if other.currency != self.currency:
            raise ValueError("Cannot add Money of different currencies!")
        new_amount = self.amount - other.amount
        if new_amount < 0:
            raise ArithmeticError("Can't have Money below zero")
        return Money(new_amount, self.currency)

    def __mul__(self, other: int) -> Self:
        return Money(self.amount * other, self.currency)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Money) and (self.amount, self.currency) == (other.amount, other.currency)


class MoneyArithmeticTests(unittest.TestCase):
    def test_adding_return_new_money(self) -> None:
        m1, m2 = Money(Decimal("1.99"), "USD"), Money(Decimal("7.99"), "USD")

        m3 = m1 + m2

        self.assertEqual(m3, Money(Decimal("9.98"), "USD"))

    def test_subtracting_returns_new_money(self) -> None:
        m1, m2 = Money(Decimal("6.99"), "USD"), Money(Decimal("1.99"), "USD")

        m3 = m1 - m2

        self.assertEqual(m3, Money(Decimal("5.00"), "USD"))

    def test_subtracting_below_zero_raises_exception(self) -> None:
        m1, m2 = Money(Decimal("6.99"), "USD"), Money(Decimal("7.99"), "USD")

        with self.assertRaises(ArithmeticError):
            m1 - m2

    def test_multiplication_of_money_by_money_raises_type_error(self) -> None:
        m1, m2 = Money(Decimal("6.99"), "USD"), Money(Decimal("7.99"), "USD")

        with self.assertRaises(TypeError):
            m1 * m2  # doesn't make sense, would it be USD**2?!

    def test_multiplication_of_money_by_int_multiplies_amount(self) -> None:
        money = Money(Decimal("1"), "USD")

        result = money * 100

        self.assertEqual(result, Money(Decimal("100"), "USD"))


if __name__ == "__main__":
    unittest.main()
