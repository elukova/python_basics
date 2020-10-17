"""
1. Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо
запускать скрипт с параметрами.
"""
from sys import argv

script_name, first_param, second_param, third_param = argv


def payroll(hours, rate, bonus):
    wages = hours * rate + bonus
    return wages


print(payroll(float(argv[1]), float(argv[2]), float(argv[3])))
