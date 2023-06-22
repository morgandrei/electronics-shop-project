"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def number():
    return Item('qwerty', 200, 50)


def test_calculate_total_price(number):
    assert number.calculate_total_price() == 10000



def test_apply_discount(number):
    assert number.apply_discount() == 200
    number.pay_rate = 0.8
    number.apply_discount()
    assert 100 * number.pay_rate == 80.0
    assert number.price == 160.0
