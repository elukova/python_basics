"""
7. Создать (не программно) текстовый файл, в котором каждая
строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль
каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с
фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

import json
profits = {}
total_pr = []
prof = 0
prof_aver = 0
i = 0
with open(r"C:\pyprojects\python_basics\hw_5_7.txt", "r") as my_file:
    for line in my_file:
        name, firm, earning, damage = line.split()
        profits[name] = int(earning) - int(damage)
        print(f"Финансовый результат {name}: {profits[name]}")
        if profits.setdefault(name) > 0:
            prof += profits.setdefault(name)
            i += 1
    total_pr.append(profits)
    if i != 0:
        prof_aver = round(prof / i, 2)
        print(f"Прибыль средняя - {prof_aver}")
        aver_prof = {"average_profit": prof_aver}
        total_pr.append(aver_prof)
        print(f"Итоговый список:{total_pr}")
    else:
        print(f"Прибыль средняя - отсутсвует. Все работают без прибыли")

with open("file_5_7.json", "w") as write_js:
    json.dump(total_pr, write_js)
    js_str = json.dumps(total_pr)
    print(f"Создан файл с расширением json со следующим содержимым: \n "
          f" {js_str}")
