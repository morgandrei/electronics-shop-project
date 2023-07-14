"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def number():
    return Item('qwerty', 200, 50)


def test_calculate_total_price(number):
    """Тест правильности расчета общей стоимости товара"""
    assert number.calculate_total_price() == 10000


def test_apply_discount(number):
    """Тест расчета скидки"""
    assert number.apply_discount() is None
    number.pay_rate = 0.8
    number.apply_discount()
    assert 100 * number.pay_rate == 80.0
    assert number.price == 160.0


def test_string_to_number():
    """Тест округления числа"""
    assert Item.string_to_number('17') == 17
    assert Item.string_to_number('17.0') == 17
    assert Item.string_to_number('-4.3') == -4


def test_new_name_setter(number):
    """Тест проверки длины наименования"""
    number.name = 'qwerty'
    assert number.name == 'qwerty'
    number.name = 'СуперСмартфон'
    assert number.name == 'СуперСмарт'


def test_item_instantiate_from_csv():
    """Тест инициализации экземпляров класса"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 0


def test___repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test___str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


# Добавьте тесты в tests/test_item.py
def test___add__():
    """Тест операции сложения экземпляров класса"""
    phone1 = Phone("iPhone 14", 120_000, 10, 2)
    item2 = Item("iPhone 14Pro", 130_000, 5)
    assert phone1 + item2 == 15
    with pytest.raises(ValueError):
        phone1.__add__(10)
