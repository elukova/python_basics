""" класс Worker, класс Position """


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        print(full_name)

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        print(total_income)


top_manager = Position("Vasya", "Vasilyok", "director", 150000, 250000)
top_manager.get_full_name()
top_manager.get_total_income()
