"""
6. Реализовать функцию int_func(), принимающую слово
из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться
с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    return word.title()


def str_func():
    words = input("Enter a string: ").split()
    res_words = []
    for el in words:
        new_el = int_func(el)
        res_words.append(new_el)
    print(res_words, end=" ")



str_func()