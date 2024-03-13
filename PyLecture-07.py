# Python Fundamentals Problems

# Problem 1:
# products = ["laptop", "smartphone", "tablet", "camera", "headphones"]
# Problem Description:
# 1. Add new product if it is not in the list
# 2. If Already in the list, already exists message should be printed
# Solution:

products = ["laptop", "smartphone", "tablet", "camera", "headphones"]
new_product = input("Enter new product: ")
if new_product in products:
    print("Already Exists")
else:
    products.append(new_product)
    print("New Product Added")
print(products)

# Solution 2:
products = ["laptop", "smartphone", "tablet", "camera", "headphones"]
new_product = input("Enter new product: ")
if new_product not in products:
    products.append(new_product)
    print("New Product Added")
else:
    print("Already Exists")

# Solution 3: using for loop
products = ["laptop", "smartphone", "tablet", "camera", "headphones"]
new_product = input("Enter new product: ")
for product in products:
    if new_product == product:
        print("Already Exists")
        break
else:
    products.append(new_product)
    print("New Product Added")

# Solution 4: using for loop with flag
products = ["laptop", "smartphone", "tablet", "camera", "headphones"]
new_product = input("Enter new product: ")
flag = False
for product in products:
    if new_product == product:
        flag = True
        print("Already Exists")
        break
if not flag:
    products.append(new_product)
    print("New Product Added")


# Solution 5: using Function and type hinting and for loop with flag
def add_product(products: list, new_product: str) -> list:
    flag = False
    for product in products:
        if new_product == product:
            flag = True
            print("Already Exists")
            break
    if not flag:
        products.append(new_product)
        print("New Product Added")
    return products


result: list[str] = add_product(products, "laptop")
print(result)
