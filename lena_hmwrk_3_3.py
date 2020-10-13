"""3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(var_1, var_2, var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    elif var_1 >= var_2:
        return var_1 + var_3
    else:
        return var_2 + var_3


print(f"Result - {my_func(int(input('Enter first argument: ')), int(input('Enter second argument: ')), int(input('Enter third argument: ')))}")
