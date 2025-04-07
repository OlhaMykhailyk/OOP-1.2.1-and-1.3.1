import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def copy(self):
        return QuadraticEquation(self.a, self.b, self.c)

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            return "infinite"

        if self.a == 0 and self.b == 0:
            return []

        if self.a == 0:
            return [-self.c / self.b]

        D = self.discriminant()

        if D < 0:
            return []
        elif D == 0:
            x = -self.b / (2 * self.a)
            return [x]
        else:
            sqrt_D = math.sqrt(D)
            x1 = (-self.b + sqrt_D) / (2 * self.a)
            x2 = (-self.b - sqrt_D) / (2 * self.a)
            return [x1, x2]

    def show(self):
        terms = []
        if self.a != 0:
            terms.append(f"{self.a}x²")
        if self.b != 0:
            sign = '+' if self.b > 0 else ''
            terms.append(f"{sign}{self.b}x")
        if self.c != 0:
            sign = '+' if self.c > 0 else ''
            terms.append(f"{sign}{self.c}")
        if not terms:
            return "0 = 0"
        return " ".join(terms) + " = 0"

def read_equations_from_file(filename):
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                a, b, c = map(float, parts)
                eq = QuadraticEquation(a, b, c)
                equations.append(eq)
    return equations
