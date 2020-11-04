"""
4. «Склад оргтехники» +
«Оргтехника» +
приём оргтехники на склад +
передачу в подразделение +
механизм валидации -
вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных
"""

from abc import ABC, abstractmethod


class Store:
    def __init__(self, name, place, square, goods):
        self.name = name
        self.place = place
        self.square = square
        self.goods = goods

    def __str__(self):
        return f"{self.name}, {self.place}, goods: {self.goods}"

    def receiving(self, new_goods):
        self.goods += new_goods

    def transfer(self, department_request):
        sending = []
        for i in department_request:
            for j in self.goods:
                if type(i) == type(j):
                    sending.append(j)
                    goods.remove(j)
                    department_request.remove(i)
        if department_request != []:
            for i in department_request:
                department_request.append(f"item {i} is missing")
                department_request.remove(i)


class OfficeEquipment(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"

    @abstractmethod
    def paperwork(self):
        pass


class Printer(OfficeEquipment):
    def paperwork(self):
        print("Я могу распечатать документ")


class Scanner(OfficeEquipment):
    def paperwork(self):
        print("Я могу отсканировать документ")


class Copier(OfficeEquipment):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

    def paperwork(self):
        print(f"Я копир {self.name} цвета {self.color}, могу скопировать документ, стою {self.price} USD")


my_copier = Copier("hpc", 500, "grey")
print(my_copier)
print(type(my_copier))
my_copier.paperwork()
my_copier_2 = Copier("fff", 300, "white")
my_printer = Printer("aaa", 400)
my_printer.paperwork()
my_printer_2 = Printer("sss", 450)
my_scanner = Scanner("ddd", 250)
my_scanner_2 = Scanner("rrr", 200)
my_scanner_2.paperwork()
goods = [my_copier, my_printer]
new_goods = [my_copier_2, my_printer_2]
my_store = Store("main", "Nevsky, 24", 300, goods)
print(my_store)
my_store.receiving(new_goods)
print(my_store)
