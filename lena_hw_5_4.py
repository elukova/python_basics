"""
4. Создать (не программно) текстовый файл
со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translator = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("hw_5_4.txt") as in_file:
    length = len(in_file.readlines())
    in_file.seek(0)
    i = 1
    new_list = []
    while i <= length:
        ex_list = in_file.readline()
        changes = ex_list.split()
        i += 1
        for x in range(len(changes)):
            for key in translator:
                if changes[x] == key:
                    changes[x] = translator[key]
                    new_str = " ".join(changes)
                    new_list.append(new_str)

with open("hw_5_4_transl.txt", "w") as out_file:
    out_file.writelines(new_list)
