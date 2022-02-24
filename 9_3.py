class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"$": wage, "+": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())} $"


worker = Position("ELON", "MASK", "CEO SpaceX Corp.", 100000, 50000)
print(worker.get_full_name())
print(worker.position)
print(worker.get_full_profit())
