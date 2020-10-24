"""
2. Реализовать класс Road
атрибуты: length (длина), width (ширина).
при создании экземпляра класса. защищенными.
Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта
для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def building_a_road(self, length, width, depth):
        print("Building a street")
        self._length = length
        self._width = width
        self.depth = depth
        mass = 25
        weight = length * width * depth * mass
        print(f"requires {round(weight/1000)} ton of asphalt")


my_street = Road()
my_street.building_a_road(1000, 10, 5)
