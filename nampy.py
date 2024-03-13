def transpose_matrix_1(matrix):
    transpose_matrix = []
    for i in range(len(matrix[0])):
        transpose_row = []
        for row in matrix:
            transpose_row.append(row[i])
        transpose_matrix.append(transpose_row)

    return transpose_matrix


def transpose_matrix_2(matrix):
    transpose_matrix = []
    for i in range(len(matrix[0])):
        transpose_row = []
        for row in matrix:
            transpose_row.append(row[i])
        transpose_matrix.append(transpose_row)

    return transpose_matrix
