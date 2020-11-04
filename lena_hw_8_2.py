"""
2. собственный класс-исключение, обрабатывающий
ситуацию деления на нуль
"""


class DivisionError(Exception):
    divisible = int(input("Введите делимое: "))
    divisor = int(input("Введите делитель: "))
    try:
        quotient = divisible / divisor
    except:
        print("Деление на ноль недопустимо")
    else:
        print(f"Результат деления {divisible} на {divisor}: {quotient}")
