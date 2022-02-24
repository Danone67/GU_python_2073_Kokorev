from colorama import Fore, init

init(autoreset=True)


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_result(self, m=25, n=5):
        return f"{Fore.BLUE}{self._length} м * {Fore.GREEN}{self._width} м * " \
               f"{Fore.RED}{m} кг * {Fore.CYAN}{n} см ={Fore.YELLOW}" \
               f" {(self._length * self._width * m * n) / 1000} т"


r = Road(20, 110)
print(r.get_result())
r = Road(111, 111)
print(r.get_result())
