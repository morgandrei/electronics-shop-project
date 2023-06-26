import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """геттер названия товара"""
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
        with open('../src/items.csv', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num: str) -> int:
        """Статический метод, возвращающий число из числа-строки"""
        return int(float(num))

