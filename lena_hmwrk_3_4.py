"""
4. Программа принимает действительное положительное число x и
целое отрицательное число y. Необходимо выполнить возведение числа x
в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень. Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
"""

base = float(input("To calculate base to negative power of index enter a base: "))
index = abs(int(input("Enter an index: ")))


def my_func(x, y):
    return round(1 / x ** abs(y), 2)


print(my_func(base, index))


base = float(input("To calculate base to negative power of index one more time enter a base: "))
index = abs(int(input("Enter an index: ")))


def my_func(x, y):
    while y > 0:
        x *= x
        y -= y
    return round(1 / x, 2)


print(my_func(base, index))
