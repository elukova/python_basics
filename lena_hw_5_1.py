"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open(r"hw_5_1.txt", "w") as user_file:
    next_string = "start string"
    while next_string != "\n":
        next_string = input("Введите следующую строку, для окончания ввода данных нажмите Enter: ") + "\n"
        user_file.writelines(next_string)

with open(r"C:\pyprojects\python_basics\hw_5_1.txt") as user_file:
    print(f"В нашем текстовом файле записано:\n{user_file.read()}")
