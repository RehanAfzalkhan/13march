# v1 = [10, 20, 30]
# v2 = [2, 3, 5]

# Solution 1:
# v3 = []
# i = 0
# for v in v1:
#     v3.append(v + v2[i])
#     i += 1
# print(v3)

# Solution 2:
# v3 = []
# for i in range(len(v1)):
#     v3.append(v1[i] + v2[i])
# print(v3)

# Solution 3:
# v3 = []
# for i, v in enumerate(v1):
#     v3.append(v + v2[i])

# print(v3)

# ....

# v1 = [3, 6, 7]
# s1 = 5

# v2 = []
# for v in v1:
#     v2.append(v + s1)

# print(v2)

# ------------

# Flatten Array

# mat = [[2, 5, 1], [3, 8, 4]]  # 2D List or Nested List -- > 1D List
# vector = []
# for v in mat:
#     vector.extend(v)

# print(vector)

# ..

# Nested List
# Nested if-else Statements
# Nested loop Statements

# List Comprehension
# Nested List Comprehension

# Dict Comprehension
# Nested Dict Comprehension


# ....

# a = 500
# b = 100
# c = 50

# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# elif b > a:
#     if b > c:
#         print(b)
#     else:
#         print(c)
# else:
#     print(c)

# find the max value

# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)


# .......

# mat = 2 * 3


# mat = [[1, 2, 3], [4, 5, 6]]
# print(mat[0][-1])             # 2D list --- Access

# .........

# mat = []
# for i in range(2):
#     vector = []
#     for j in range(3):
#         vector.append(j)
#     mat.append(vector)

# print(mat)


# ----

# v1 = [2, 5, 7]
# v2 = [1, 6, 7]

# mat = [v1] + [v2]
# print(mat)


# ....................

matrix = [[2, 4, 6], [1, 2, 4], [3, 7, 1], [2, 7, 1]]

# print(len(matrix))

# for row in matrix:
#     print(row[2])

# transpose_matrix = []
# for i in range(len(matrix[0])):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose_matrix.append(transpose_row)

# print(transpose_matrix)

# Solution 2

# transpose_matrix = []
# for i in range(len(matrix[0])):
#     transpose_row = [row[i] for row in matrix]
#     transpose_matrix.append(transpose_row)

# print(transpose_matrix)

# Solution 3

# transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transpose_matrix)

# print(list(zip(*matrix)))


# ------------

# List Comprehension -- list + for + if

# Syntax 1: [expression for var in iterable if condition]

# users = ["ahmad", "bilal", "anas", "khalil"]
# new_users = []

# for user in users:
#     new_users.append(user.upper())

# print(new_users)


# Solution 1: List new_users
users = ["ahmad", "bilal", "anas", "khalil"]
new_users = [user.upper() for user in users]
# print(new_users)

sq = [i**2 for i in range(1, 6)]
# print(sq)


users = ["ahmad", "bilal", "anas", "khalil"]
len_users = [len(user) for user in users]
# print(len_users)


users = ["ahmad", "bilal", "anas", "khalil"]
new_users = [user for user in users if len(user) > 4]
# print(new_users)

new_users = []
for user in users:
    if len(user) > 4:
        new_users.append(user)

# print(new_users)

# Ternary Operator -- Conditional Statement

# v1 = [10, 20, 30]
# v2 = [2, 3, 5]

# v3 = []
# for i in range(len(v1)):
#     v3.append(v1[i] + v2[i])

# v4 = [v1[i] + v2[i] for i in range(len(v1))]

# print(v3)
# print(v4)


matrix = [[2, 5, 1], [3, 8, 4]]

# vector = []
# for v in matrix:
#     vector.extend(v)

# vector = []
# for row in matrix:
#     for value in row:
#         vector.append(value)

# vector = [expression for var in iterable]
# vector = [value for row in matrix for value in row]

# print(vector)

# -----------

# list_comp_1 = [expression for var in iterable]
# list_comp_2 = [expression for var in iterable if condition]

# list_comp_3 = [value for row in matrix for value in row]
# list_comp_4 = [[expression] for var in iterable]


# matrix = [[2, 4, 6], [1, 2, 4], [3, 7, 1], [2, 7, 1]]

# transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# print(transpose_matrix)


# ........

# 1. Bubble Sort
# 2. rizwan@example.com
# a. username           rizwan
# b. domain             example.com
# 3. domain extension   com

# using function

# Exception Handling


# Modules
# 1. Built-in Modules
# 2. User-Defined Modules

# Module --- Collection of functions, classes or attributes (fields) or global varibales

# import nampy
# import nampy as na
# from nampy import transpose_matrix_1

# matrix = [[2, 4, 6], [1, 2, 4], [3, 7, 1], [2, 7, 1]]
# T = transpose_matrix_1(matrix)

# print(T)


# import nampy as na

# result_1 = na.transpose_matrix_1()
# result_2 = na.transpose_matrix_2()

# print(result_1)


# Module  -- File
# Package -- Folder


#  -----------------------------


# AI Tic Tac Toe


def draw_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]}")
    # ...


game_board = [" "] * 10
game_board[9] = "X"
draw_board(game_board)
