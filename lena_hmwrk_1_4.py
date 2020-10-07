#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.
source = int(input("Введите целое положительное число: "))
s_max = source % 10
source = source // 10
while source > 0:
    if source % 10 > s_max:
        s_max = source % 10
    source = source // 10
print(s_max)