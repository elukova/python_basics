"""2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке."""

with open(r"C:\pyprojects\python_basics\hw_5_2.txt") as f_obj:
    f_strings = f_obj.readlines()
    str_sum = len(f_strings)
    print(f"В нашем файле {str_sum} строк.")
    for n_str in f_strings:
        num_str = f_strings.index(n_str) + 1
        words_str = len(list(n_str.split()))
        print(f"В {num_str} строке {words_str} слов.")
