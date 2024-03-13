# Python Functional Programming

# Python Functional Programming - Lambda, Map, Filter, Reduce

# Lambda
# Lambda is a small anonymous function that can take any number of arguments, 
# but can only have one expression.
# Syntax: lambda argument(s) : expression

# Example 1:
# def greet(name): 
#     return "Hi, " + name

# greet = lambda name : "Hi, " + name
# result = greet("Junaid")
# print(result)

# Example 2:
# def add(x, y):
#     return x + y

# add = lambda x, y : x + y
# result = add(5, 3)
# print(result)

# ...


# students: list[dict] = [
#     {"name": "Ahmad", "age": 24},
#     {"name": "Bilal", "age": 27},
#     {"name": "Khalil", "age": 25}
# ]

# # def increase_age(student: dict) -> dict:
# #     student["age"] += 1
# #     return student

# students_2024: list[dict] = []
# for student in students:
#     student["age"] += 1
#     students_2024.append(student)

# print(students)

# ---

# students: list[dict] = [
#     {"name": "Ahmad", "age": 24},
#     {"name": "Bilal", "age": 27},
#     {"name": "Khalil", "age": 25}
# ]

# def increase_age(student: dict) -> dict:
#     student["age"] += 1
#     return student

# students_2024: list[dict] = []
# for student in students:
#     students_2024.append(increase_age(student))

# print(students)

#-------

# students: list[dict] = [
#     {"name": "Ahmad", "age": 24},
#     {"name": "Bilal", "age": 27},
#     {"name": "Khalil", "age": 25}
# ]

# def increase_age(student: dict) -> dict:
#     student["age"] += 1
#     return student

# students_2024 = list(map(increase_age, students))
# print(students_2024)

# -------

