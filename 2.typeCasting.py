# typecasting = The process of converting a value of one data type to anothe.
# (string, integer, float, boolean)
#Explicit vs Implicit

#1. Explicit

name = "parvaj"
age= 20
gpa= 3.8
is_student = True

# print(is_student)

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

age = float(age)
# print(type(age))

gpa = int(gpa)
# print

age = bool(age)
# print(age)

#2. Implecit

x= 2
y = 1.3
x = x*y
print(x)