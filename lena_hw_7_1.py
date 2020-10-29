"""
1. Matrix
"""

from copy import deepcopy


class Matrix:

    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)
    # при изменении списков, от которых была сконструирована матрица,
    # содержимое матрицы не будет изменяться. Для данной задачи допустим,
    # списки состоят из чисел, не пусты и имеют одинаковый размер.

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_matrix)
other_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_matrix + other_matrix)
