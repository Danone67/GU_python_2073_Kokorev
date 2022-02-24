class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(
            ' '.join(
                [f"{i:4}" for i in line]
            )
            for line in self.data
        )

    def __add__(self, other):
        if len(self.data) == len(other.data):
            m = [[self.data[line][_] + other.data[line][_] for _ in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        else:
            return f'Ошибка размерностей матриц'


m_1 = [[3, 32, 2], [2, 4, 6], [11, 22, 3]]
m_2 = [[5, 23, 33], [9, 23, -54], [12, 3, 16]]

mtrx_1 = Matrix(m_1)
print(f'Матрица №1:\n{mtrx_1}')
mtrx_2 = Matrix(m_2)
print(f'Матрица №2:\n{mtrx_2}')
print(f'Сумма матриц:\n{mtrx_1 + mtrx_2}')
