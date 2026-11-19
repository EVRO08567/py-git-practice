from calculator import Calculator

calc = Calculator()

print("Сложение:", calc.add(10, 5))
print("Вычитание:", calc.subtract(10, 5))
print("Умножение:", calc.multiply(10, 5))
print("Деление:", calc.divide(10, 5))

try:
    print(calc.divide(10, 0))
except ValueError as error:
    print(error)
