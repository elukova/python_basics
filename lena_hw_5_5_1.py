"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""


def summary():
    try:
        with open('hw_5_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(f"Сумма чисел в файле: {sum(map(int, my_numb))}")
    except ValueError:
        print("Неправильно набран номер. Ошибка ввода-вывода")


summary()
