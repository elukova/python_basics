"""
5. Stationery
"""


class Stationery:

    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    title = "pen"

    def draw(self, title):
        print(title)
        print("it's a pen line")


p = Pen()
p.draw(title="pen")


class Handle(Stationery):

    title = "handle"

    def draw(self, title):
        print(title)
        print("it's a handle line")


class Pencil(Stationery):
    title = "pencil"

    def draw(self, title):
        print(title)
        print("it's a pencil line")


pc = Pencil()
pc.draw("pencil")

hl = Handle()
hl.draw("handle")