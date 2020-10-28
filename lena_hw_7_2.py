"""
2. Реализовать проект расчета суммарного расхода ткани на производство
одежды.
Не получилось проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название.
class Clothes(ABC):

    all_material = 0

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_material(self, value):
        pass


# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
class Suit(Clothes):

    def __init__(self, name):
        super().__init__(name)

    def get_material(self, high):
        material = round((2 * high + 0.3), 2)
        Clothes.all_material += material
        print(f"Your {self.name} high {high} takes {material} meters material")
        print(f"You have used {Clothes.all_material} meters material at all")


class Coat(Clothes):

    def __init__(self, name):
        super().__init__(name)

    def get_material(self, size):
        material = round((size / 6.5 + 0.5), 2)
        Clothes.all_material += material
        print(f"Your {self.name} size {size} takes {material} meters material")
        print(f"You have used {Clothes.all_material} meters material at all")

    @property
    def know_how(self):
        return f"I still can't get decorators at all(( Coat {self.name}"


my_suit = Suit("dark_suit")
Suit.get_material(my_suit, 1.8)  # interesting

my_coat = Coat("red_coat")
my_coat.get_material(42)
print(my_coat.know_how)
