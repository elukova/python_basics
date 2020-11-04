"""комплексные числа"""


class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __str__(self):
        sign = "+" if self.b >= 0 else ""
        return f"{self.a}{sign}{self.b}*i"

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a, self.b * other.b)


c1 = Complex(1, 2)
print(c1)
c2 = Complex(3, -4)
print(c2)
c3 = c1 + c2
print(c3)
print(c1*c2)
