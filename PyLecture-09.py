# import array  # Built-in module for array manipulation

# v1 = array.array("I", [1, 2, 3, 4, 53])  # Create an array of integers

# print(v1)  # Print the array

# v1.insert(2, -6)  # Insert 6 at index 2

# print(v1)  # Print the array

#  ------------

# int()
# float()
# list()

# Python List vs Array
# 1. List can store different types of data, while array can store only one
# type of data
# 2. List is a built-in function, while array is a built-in module
# 3. List is more flexible than array in terms of operations
# 4. Python Array is slower than Python List in terms of operations
# 5. List is more memory efficient than array
# 6. List is more powerful than array

# --------------

# Python Array - 1D Array
# import array  # Built-in module for array manipulation
# s1 = array.array("I", [1])
# v1 = array.array("I", [1, 2, 3, 4, 53])  # Create an array of integers


# Python Dimensions of Array or List

# 0D Array or List            - Scalar        - 0D Tensor
# 1D Array or List            - Vector        - 1D Tensor
# 2D NumPy Array or List      - Matrix        - 2D Tensor
# 3D NumPy Array or List      - Tensor        - 3D Tensor
# 4D NumPy Array or List      - Tensor        - 4D Tensor

# --------------


# # Bubble Sort Algorithm
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr


# sorted_values = bubble_sort([9, 6, 8, 1, 2])
# print(sorted_values)

# - ----------------------------

# print "xyz"           # SyntaxError: Missing parentheses in call to 'print'. Did you mean print("xyz")?
# x = "xyz" + 5         # TypeError: can only concatenate str (not "int") to str
# print(x)              # NameError: name 'x' is not defined
# print(10 / 0)  # ZeroDivisionError: division by zero
# values = [1, 2, 3, 4, 5]
# print(values[10])  # IndexError: list index out of range
# dict1 = {"name": "Javed", "age": 25}
# print(dict1["address"])  # KeyError: 'address'

# ----------------------------

# Python Exception Handling
# Python Exception Handling is a mechanism to handle runtime errors
# such as SyntaxError, TypeError, IndexError, KeyError, etc.

# Key Components of Python Exception Handling:
# 1. try block     - One try block  - Mandatory - The code that might raise an exception
# 2. except block  - One or more except blocks - Mandatory - The code that handles the exception
# 3. else block    - One else block - Optional - The code that runs if no exception is raised
# 4. finally block - One finally block - Optional - The code that runs regardless of the result


# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr


# try:
#     values = [9, 6, 8, 1, 2, y]  # list of integers
#     sorted_values = bubble_sort(values)  # Call the function
# except (ZeroDivisionError, TypeError, IndexError) as err:
#     print(err)  # Print the error message
#     # print("List contains non-integer values")  # Print the error message
# except:
#     print("Something went wrong")
# else:
#     print(sorted_values)  # Print the sorted values
# finally:
#     print("The program has been executed")


# -------------

# Python Control Flow Statements
# pass, break, continue, else, return, yield

# pass - Do nothing
# break - Exit the loop
# continue - Skip the current iteration
# else - Execute the code if no exception is raised in the try block (try)
# else - Execute the code if no break statement is executed          (for, while)
# return - Exit the function
# yield - Return a value from a generator


# Pass Statement
# 1. pass with if statement
# x = 3
# if x > 5:
#     pass
# else:
#     print("x is less than 5")

# 2. pass with function
# def my_function():
#     pass

# 3. pass with class
# class MyClass:
#     pass


# Break Statement
# for i in range(10):
#     if i == 50:
#         break
#     print(i)
# else:
#     print("The loop has been executed")

# Continue Statement
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("The loop has been executed")


# ---------------

# Python Ternary Operator or Conditional Expression

# Syntax: [on_true] if [expression] else [on_false]

# Example: with if-else statement
# marks = 80
# result = ""
# if marks >= 40:
#     result = "Pass"
# else:
#     result = "Fail"
# print(result)

# Example: with ternary operator
# marks = 80
# result = "Pass" if marks >= 40 else "Fail"
# print(result)

# Example: a, b, c, d grade system using if-else statement
# marks = 80
# grade = ""
# if marks >= 90:
#     grade = "A"
# elif marks >= 80:
#     grade = "B"
# elif marks >= 70:
#     grade = "C"
# else:
#     grade = "D"
# print(grade)

# Example: a, b, c, d grade system using ternary operator
# marks = 80
# grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D"


# ------------

