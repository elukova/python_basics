"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open("hw_5_6.txt") as f_obj:
    length = len(f_obj.readlines())
    f_obj.seek(0)
    j = 1
    subj_hours_dict = {}
    while j <= length:
        subj_hours = 0
        examp_str = f_obj.readline()
        j += 1
        n_list = examp_str.split()  # исходная строка на список строк
        for every_str in n_list:  # каждую строку из списка
            work_list = []
            for el in every_str:
                work_list.append(el)  # делим на cписок символов
                part_hours = ["0"]
                for i in work_list:  # в каждом списке символов исчем цифры
                    if i.isdigit() == True:
                        part_hours.append(i)
            part_hours_str = "".join(part_hours)
            int_hours = int(part_hours_str)
            subj_hours = subj_hours + int_hours
        subj_hours_dict.update({n_list[0]: subj_hours})
    print(subj_hours_dict)


