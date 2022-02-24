class ComplexNumber:
    a: float
    b: float

    def __init__(self,  a: float, b: float):
        self.a = a
        self.b = b

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other: 'ComplexNumber'):

        num1 = (self.a * other.a) + (self.b * other.b * -1)
        num2 = (self.a * other.b) + (self.b * other.a)

        return ComplexNumber(num1, num2)

    def __str__(self):
        return f"{self.a} + {self.b}i"


num_1 = ComplexNumber(15, 7)
num_2 = ComplexNumber(2, 6)

print(f"Результат сложения: {num_1 + num_2}")

print(f"Результат умножения: {num_1 * num_2}")
