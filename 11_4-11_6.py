# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

import typing


class Storage:

    def __init__(self):
        self.__storage = {}

    def take_to_storage(self, equipment: 'OfficeEquipment', count: int):
        if equipment in self.__storage:
            self.__storage[equipment]['count'] += count
            return
        self.__storage[equipment] = dict(
            equipment=equipment,
            count=count,
        )

    def issue(
            self, type_equipment: typing.Type['OfficeEquipment'], count: int, args_of_equipment
    ):
        try:
            position = next(v for k, v in self.__storage.items()
                            if isinstance(v['equipment'], type_equipment)
                            and all(v['equipment'][arg] == arg_val for arg, arg_val in args_of_equipment.items())
                            and v['count'] >= count)
        except StopIteration:
            print('подходящей позиции нет на складе')
            return
        self.__storage[position['equipment']]['count'] = position['count'] - count
        print(f"выдано {count} {str(position['equipment'])}")
        return position['equipment'], count

pass




#НЕ успел доделать