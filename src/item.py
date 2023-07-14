import csv
import os


class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла"""

    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """Геттер названия товара"""
        return self.__name

    @name.setter
    def name(self, name) -> None:
        """Сеттер на название товара, в зависимости от длины"""
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all = []
        filepath = os.path.join(os.path.dirname(__file__), 'item.csv')
        try:
            with open(filepath, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not all(key in row for key in ['name', 'price', 'quantity']):
                        raise InstantiateCSVError
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except InstantiateCSVError as m:
            print(m)

    @staticmethod
    def string_to_number(num: str) -> int:
        """Статический метод, возвращающий число из числа-строки"""
        return int(float(num))

    def __add__(self, other):
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
