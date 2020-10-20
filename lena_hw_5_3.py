"""3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open("hw_5_3.txt") as f_obj:
    f_strings = f_obj.readlines()
    poor = []
    sal = []
    for n_str in f_strings:
         word_list = n_str.split()
         for ev_str in word_list:
                 try:
                     float(ev_str)
                     sal.append(float(ev_str))
                     if float(ev_str) < 20000.00:
                         poor.append(word_list[word_list.index(ev_str)-1])
                 except: ValueError
    print(f"Оклад меньше 20.000: {', '.join(poor)}, средний оклад: {sum(map(int, sal)) / len(sal)}")


