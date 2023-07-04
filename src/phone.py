from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """Вызываем метод базового класса"""
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return str(f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})")

    @property
    def number_of_sim(self):
        if isinstance(self.value, int) and self.value > 0:
            return self.value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    @number_of_sim.setter
    def number_of_sim(self, value):
        self.value = value
