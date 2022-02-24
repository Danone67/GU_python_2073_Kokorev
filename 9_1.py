import time
from colorama import Fore, Back, Style, init
from itertools import cycle

init()


class TrafficLight:
    __color = [['КРАСНЫЙ', 7, Back.RED, Fore.BLACK], ['ЖЕЛТЫЙ ', 2, Back.YELLOW, Fore.BLACK],
               ['ЗЕЛЕНЫЙ', 4, Back.GREEN, Fore.BLACK], ['ЖЕЛТЫЙ ', 2, Back.YELLOW, Fore.BLACK]]

    def running(self):
        count = 0
        for i in cycle(self.__color):
            if count > 10:
                print('Светофор устал')
                break
            print(f'{i[2]}{i[3]}{i[0]}', end='')
            print(Style.RESET_ALL)
            time.sleep(i[1])
            count += 1


a = TrafficLight()
a.running()
