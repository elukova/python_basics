# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена
# составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число —
# номер дня.
# Например: a = 2, b = 3.
km_goal = int(input("Поставьте цель - введите длину пробежки в километрах: "))
km_act = int(input("Введите длину первой пробежки в километрах: "))
day = 1
while km_act < km_goal:
    km_act = km_act * 1.1
    day = day + 1
print("Если каждый день Вы будете бегать на 10% больше, чем в предыдущий, Вы достигнете цели через", day, "дней")