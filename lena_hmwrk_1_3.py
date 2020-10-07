# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
dgt_str_1 = input("Введите целое число: ")
dgt_str_2 = dgt_str_1 + dgt_str_1
dgt_str_3 = dgt_str_1 + dgt_str_2
dgt_res = int(dgt_str_1) + int(dgt_str_2) + int(dgt_str_3)
print(dgt_res)