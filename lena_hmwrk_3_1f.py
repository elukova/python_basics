"""Реализовать функцию, принимающую два числа (позиционные аргументы)
 и выполняющую их деление. Числа запрашивать у пользователя,
 предусмотреть обработку ситуации деления на ноль.
 """


def my_div():
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
    try:
        dividend / divisor
    except ZeroDivisionError:
        return "Can not be divided by zero"
    return round((dividend / divisor), 2)


print(f"Quotient : {my_div()}")
