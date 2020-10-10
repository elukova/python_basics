# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

work_list = input("Enter your string, please: ").split()
res_list = []
for el in work_list:
    if len(el) > 10:
        el = el[:10]
        res_list.append(el)
    else: res_list.append(el)

for ind, el in enumerate(res_list, 1):
    print(ind, el)
