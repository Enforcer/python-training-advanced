"""
Turn Money into Value Object:

- make amount and currency private attributes and expose read-only properties for them
- validate amount and currency
    - amount: must be positive or 0
    - amount: only up to 2 decimal places
    - currency: only supported currencies are USD and EUR
"""
import unittest
from decimal import Decimal
from enum import StrEnum, auto
from typing import Any, Self


class Currency(StrEnum):
    EUR = "EUR"
    USD = "USD"


class Money:
    def __init__(self, amount: Decimal, currency: str) -> None:
        try:
            self._currency = Currency(currency)
        except ValueError:
            raise ValueError(f"Currency {currency} is not supported")

        if amount < 0:
            raise ValueError(f"Amount of money must not be negative")
        quantized = amount.quantize(Decimal("0.01"))
        if quantized != amount and amount != Decimal("0"):
            raise ValueError(f"Invalid amount {amount}")

        self._amount = quantized
        self._currency = Currency(currency)

    @property
    def amount(self) -> Decimal:
        return self._amount

    @property
    def currency(self) -> Currency:
        return self._currency

    def __add__(self, other: Any) -> Self:
        if not isinstance(other, Money):
            raise TypeError
        if other.currency != self.currency:
            raise ValueError("Cannot add Money of different currencies!")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: Any) -> Self:
        if not isinstance(other, Money):
            raise TypeError
        if other.currency != self.currency:
            raise ValueError("Cannot add Money of different currencies!")
        new_amount = self.amount - other.amount
        if new_amount < 0:
            raise ArithmeticError("Can't have Money below zero")
        return Money(new_amount, self.currency)

    def __mul__(self, other: Any) -> Self:
        if not isinstance(other, int):
            raise TypeError

        return Money(self.amount * other, self.currency)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Money) and (self.amount, self.currency) == (other.amount, other.currency)


class MoneyValueObjectTests(unittest.TestCase):
    def test_unsupported_currency_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            Money(Decimal("10.0"), "PLN")

    def test_negative_amount_is_not_allowed(self) -> None:
        with self.assertRaises(ValueError):
            Money(Decimal("-10.0"), "USD")

    def test_zero_amount_is_allowed(self) -> None:
        money = Money(Decimal(), "USD")

        self.assertEqual(money.amount, Decimal("0"))

    def test_cannot_set_amount(self) -> None:
        money = Money(Decimal("1.99"), "USD")

        with self.assertRaises(AttributeError):
            money.amount = Decimal("2.99")

    def test_cannot_set_currency(self) -> None:
        money = Money(Decimal("1.99"), "USD")

        with self.assertRaises(AttributeError):
            money.currency = "EUR"


if __name__ == "__main__":
    unittest.main()
