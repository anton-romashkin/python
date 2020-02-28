class Matrix:
    def __init__(self, m_list):
        self.matrix = m_list

    def __add__(self, other):
        new_list = []
        for i, j in zip(data_matrix, other):
            result = [x + y for x, y in zip(i, j)]
            new_list.append(result)
            self.matrix = new_list

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in line]) for line in self.matrix])


data_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

matrix1 = Matrix(data_matrix)
print(matrix1, '\n')

add_matrix = [[4, 4, 4], [5, 5, 5], [1, 0, 5]]
matrix1 + add_matrix
print(matrix1)
