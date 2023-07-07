from src.item import Item


class MixinLang:
    lang = 'EN'

    def __init__(self):
        self.__language = self.lang

    def change_lang(self):

        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self):
        """Геттер языка раскладки клавиатуры"""
        return self.__language


class Keyboard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
