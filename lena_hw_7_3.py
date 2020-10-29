"""
3. Реализовать программу работы с органическими клетками.
"""
# В конструкторе инициализировать
# параметр, соответствующий количеству клеток (целое число).


class Cell:

    cells_amount = 0

    def __init__(self, quantity):
        self.quantity = quantity
        Cell.cells_amount += 1
        print(f"Создана {Cell.cells_amount} клетка из {self.quantity} ячеек")

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity <= other.quantity:
            print("Уменьшаемая клетка меньше или равна вычитаемой, новая клетка не создана")
        else:
            return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        new_quantity = self.quantity / other.quantity
        return Cell(round(new_quantity))

    def make_order(self, row):
        w_str = "*" * row
        list_of_str = []
        i = self.quantity // row
        while i > 0:
            list_of_str.append(w_str)
            i -= 1
        i = self.quantity % row
        if i > 0:
            w_str = "*" * i
            list_of_str.append(w_str)
        result = "\n".join(list_of_str)
        print(result)

    def make_order_2(self, row):
        res_str = "*"
        i = 1
        while i <= self.quantity:
            if i % row == 0:
                res_str = res_str + "*"
                res_str = res_str + "\n"
                i += 1
            else:
                res_str += "*"
                i += 1
        print(res_str)

cells1 = Cell(33)
cells2 = Cell(9)
cells3 = cells1 + cells2
cells4 = cells2 - cells1
cells4 = cells1 - cells2
cells5 = cells1 * cells2
cells6 = cells1 / cells2
cells1.make_order(9)
cells1.make_order(9)
