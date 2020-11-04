"""
3. класс-исключение должен проверять на наличие только чисел
"""


class InputNumberError(Exception):
    list_of_numbers = []
    input_data = input("Введите число (для выхода нажмите Q): ")

    while input_data != "q" and input_data != "Q":
        try:
            number = float(input_data)
        except:
            print("Вы ввели не число")
            input_data = input("Введите число (для выхода нажмите Q): ")
        else:
            list_of_numbers.append(number)
            input_data = input("Введите число (для выхода нажмите Q): ")

    print(f"Ваш список чисел: {list_of_numbers}")

