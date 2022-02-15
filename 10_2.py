from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size, name):
        self.size = size
        self.name = name

    @abstractmethod
    def cloth_amount(self):
        pass


class Suit(Clothes):

    @property
    def cloth_amount(self):
        return 2 * self.size + 0.3


class Coat(Clothes):

    @property
    def cloth_amount(self):
        return self.size / 6.5 + 0.5


my_coat = Coat(6.5, 'пальто')
print(f'Для {my_coat.name} потребуется {my_coat.cloth_amount} п.м. ткани')

my_suit = Suit(2, 'смокинга')
print(f'Для {my_suit.name} потребуется {my_suit.cloth_amount} п.м. ткани')
