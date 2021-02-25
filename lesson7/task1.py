class Matrix:
    def __init__(self, mymatrix: list[list]):
        self.matrix = mymatrix
        if len(self.matrix) < 2 or len(self.matrix[0]) < 2:
            raise ValueError('Matrix is at least 2x2')
        self.matrix_size = frozenset([(len(self.matrix), len(row)) for row in self.matrix])
        if len(self.matrix_size) != 1:
            raise ValueError(f'Invalid Matrix Size: {self.matrix_size}')

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Cannot add objects if different types')
        if other.matrix_size != self.matrix_size:
            raise ValueError('Cannot add matrices of different size')
        result = []
        for i in zip(self.matrix, other.matrix):
            result.append([sum([k, n]) for k, n in zip(*i)])
        return Matrix(result)


a = [[1, 2, 3], [1, 2, 3]]

b = Matrix(a)
c = Matrix(a)
print(b + c)

# nrow = len(a)
# c = frozenset([(nrow, len(row)) for row in a])
#
# for row in a:
#     print(row)
# print(len(c))
