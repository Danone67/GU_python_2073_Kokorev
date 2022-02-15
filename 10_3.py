class Cell:

    def __init__(self, cells: int) -> None:
        self.__cells = cells

    def __add__(self, other: 'Cell'):
        return Cell(self._get_size() + other._get_size())

    def __sub__(self, other: 'Cell'):
        if self._get_size() < other._get_size():
            raise ValueError("Результат отрицательный")

        return Cell(self._get_size() - other._get_size())

    def __mul__(self, other: 'Cell'):
        return Cell(self._get_size() * other._get_size())

    def __floordiv__(self, other: 'Cell'):
        return Cell(self._get_size() // other._get_size())

    def _get_cells(self) -> str:
        return str(self).replace("(", "").replace(")", "")

    def _get_size(self) -> int:
        return self._get_cells().count("*")

    def __str__(self) -> str:
        return f"({'*'*self.__cells})"

    def make_order(self, split_cell) -> str:
        if split_cell == 0:
            raise ValueError("Невозможно поделить на 0")

        if split_cell >= self._get_size():
            return self._get_cells()

        size = self._get_size()

        return "".join([f"{x}\n" if i % split_cell == 0 and i != size
                        else x
                        for i, x in enumerate(self._get_cells(), start=1)])


cell_1 = Cell(3)
cell_2 = Cell(2)
print(f'Клетка 1: {cell_1}')
print(f'Клетка 2: {cell_2}')
print(f'Сложение: {cell_1 + cell_2}')
print(f'Вычитание: {cell_1 - cell_2}')
print(f'Умножение: {cell_1 * cell_2}')
print(f'Деление: {cell_1 // cell_2}')
print(f'Организация по рядам:\n{cell_1.make_order(2)}')
