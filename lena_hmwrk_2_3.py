# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень).
# Напишите решения через list и через dict.
# Вариант 1 - через список
month = int(input("Enter the month number: "))
seasons = ["winter", "spring", "summer", "autumn"]
months =[[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
if month in months[0]:
    print("The season is", seasons[0])
elif month in months[1]:
    print("The season is", seasons[1])
elif month in months[2]:
    print("The season is", seasons[2])
else: print("The season is", seasons[3])

# Вариант 2 - через словарь
month = int(input("Enter the month number: "))
year = {"winter": 1, "spring": 2}
print(year["winter"])
