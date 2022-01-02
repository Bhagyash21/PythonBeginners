class Shape:
    argu = 2
    def calculate(self, var):
        res = self.argu + var
        return res
obj = Shape()
obj = obj.calculate(10)
print(obj)

#encapsulation
# import math as m
# class shape:
#     __side = 2
#     arg = 3
#     def __init__(self,radius):
#         self.radius=radius
#     def area_circle(self):
#         return round(self.radius*self.radius*3.14)
#     def perimeter_circle(self):
#         return round(2*3.14*self.radius)
#
# circle=shape(10)
# print(circle.area_circle())
# print(circle.perimeter_circle())
# print(circle.arg)
# print(circle.side)

#inheritance

# class Parent:
#     parentAge = 50
#     def parentPrint(self, parentAge):
#         print("The age of Parent is",parentAge)
# class Child(Parent):
#     childAge = 10
#     def childPrint(self,childAge):
#         print("The age of child is",childAge)
#
# childobj = Child()
# childobj.parentPrint(10)


#Program
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# output = [int(x) for x in numbers if x > 0]
# print(output)

#Use list comprehension
sentence = "the quick brown fox jumps over the lazy dog"
ctr = [len(x) for x in sentence.split() if x != "the"]
print(ctr)

#Above program using for loop
# sentence = "the quick brown fox jumps over the lazy dog"
# # s = sentence.split()
# # print(s)
# for x in sentence.split():
#     if x != "the":
#         print(len(x))

# Program
# myList = [1,2,3,4,5]
# result = [x**2 if x%2 == 0 else x**3 for x in myList]
# print(result)

import re
s='PythonForPython: A computer science portal for progs'
p="portal"
match=re.search(p,s)
print("Start Index of Portal word",match.start())
print("End Index of Portal word",match.end())


