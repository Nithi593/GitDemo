class BasicCalculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


obj = BasicCalculator(10, 5)

print(f"Addition: {obj.addition()}")
print(f"Subtraction: {obj.subtraction()}")
print(f"Multiplication: {obj.multiplication()}")
print(f"Division: {obj.division()}")

print(f"Addition: {obj.addition()}")
print(f"Subtraction: {obj.subtraction()}")
print(f"Multiplication: {obj.multiplication()}")
print(f"Division: {obj.division()}")
