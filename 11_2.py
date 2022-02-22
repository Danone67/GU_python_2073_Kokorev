class Math:
    num_1: int
    num_2: int

    @staticmethod
    def division(num_1: int, num_2: int):
        if num_2 == 0:
            raise DivisionByZeroError
        else:
            return round(num_1 / num_2, 2)


class DivisionByZeroError(Exception):
    def __str__(self):
        return "На ноль делить невозможно"


try:
    print(Math.division(100, 0))
except DivisionByZeroError as exception:
    print("Ошибка! На ноль делить нельзя")
