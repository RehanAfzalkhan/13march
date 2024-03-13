# # python object oriented programming
# -----------------------------------------
# # python classes
# # python class is a blueprint for creating bojects.
# # logical entity that has some attributes and methods.
# # constructor,
# ## instance class
# # the class whom we can create instances and we can access them too.
# # example1:
# class MyClass:
#     pass

# --------------------------------------------
# MyClass()  # constructor calling(),create new instance of class,object initiation
# # python objects
# print(type(MyClass()))
# -----------------------------------------
# python instance variable or object/instance attribute
# instance variables are uniue to each instance of a class.
# they are defined inside the construtor __init__ method.
# they are accessed using a . dot notation.
# class MyClass:
#     def __init__(self, attr_1, attr_2) -> None:  # creating construtor
#         # self store the reference of object
#         self.instance_attr1 = attr_1
#         self.instance_attr2 = attr_2

#     # getter method
#     def method_1(self):
#         return self.instance_attr1


# instace_1 = MyClass(10, 20)
# instace_2 = MyClass(30, 40)
# # print(instace_1.instance_attr1)
# # print(instace_1.instance_attr2)
# # print(instace_2.instance_attr1)
# # print(instace_2.instance_attr2)
# Value = instace_2.method_1()
# print(Value)
# _--------------------
# python instance methods(regular methods)

# instance methods are defined inside a class and
# are used to get the contents of and instance
# they can also be used to perform operations with
# the attributes of our objects.
# liek the __init__ the first argument is always self.
# example


# class NeuralNetworks:  # create class
#     def sigmoid(self, x):
#         return 1 / (1 + math.exp(-x))

#     def train(self):
#         print("train model")

#     def predit(self):
#         print("predict model")


# mn_1 = NeuralNetworks()
# # mn_2 = NeuralNetworks()
# # mn_1.train()
# # mn_2.train()

# # ------------------------------
# # python class variables
# # class variables are shared among all insatances of a class.
# # they are defined inside the lass and outside of any method
# # they are accessed using the class name
# # they are used to store info that is shared among all instances

# # example
# # class MyClass:
# #     class_attr = "shared_value"  # create class attribute
# #     class_attr = "new_shared_value"  # assigned new value


# # instance1 = MyClass()
# # instance1.class_attr = "instance_1_value"  # create instance variable
# # instance2 = MyClass()  # create class instance
# # print(MyClass.class_attr)  # access class attr with class name
# # print(instance1.class_attr)  # access class attt with instance
# # print(instance2.class_attr)
# # example2
# class MyClass:
#     def __init__(self) -> None:
#         self.x = 5
#         self.y = 10


# instance1 = MyClass()
# instance1.x = 50
# instance2 = MyClass()
# print(instance1.x)
# print(instance2.y)

# -------------------
# python class methods
# class methods are methods that are bound to the lass,
# rather than a object/instance
# they are defined using the @classmethod decorator
# they can be calle don the classiteself, rather than on an
# instance fo the calss.
# they can be used to modify class state that applies aross
# all instances fo the class.
# they can be use as alternative constructors.

# example
# class MyClass:
#     class_attrbute = "shared_value"

#     @classmethod
#     def class_method(cls):
#         return cls.class_attrbute


# print(MyClass.class_method())


# example2
# they can be use as alternative constructors.
# class MyClass:
#     def __init__(self, value: int) -> None:
#         self.x = value

#     @classmethod
#     def from_string(cls, value):
#         if value.lower() == "true":
#             value = True
#         else:
#             value = False
#         return cls(value)


# obj1 = MyClass(50)
# print(obj1)
# obj2 = MyClass.from_string("True")
# print(obj2)

# -----------
# python constructor and python destructor
# class MyClass:
#     def __init__(self) -> None:
#         print("contructor called")
#     def __init__(slef):
