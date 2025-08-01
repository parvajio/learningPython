# collection = single variable used to store multiple values
#List = [] ordered, changeable. Duplicates Ok
#set = {} unordered, immutable, but add/remove ok. No duplicates
#Tuple = () ordered, unchangeable. Duplicate ok. Faster
from itertools import count

#List
fruits = ["apple", "banana", "Mango","COCONUT"]

# print(fruits)
# print(fruits[0])
# print(fruits[0:2])  #0-2 index
# print(fruits[::2]) #show every second element
# print(fruits[::-1]) #show every element in backword

# for fruit in fruits:
#     print(fruit)

# print(dir(fruits))
# print(help(fruits))

# print(len(fruits))
# print("apple" in fruits)
# fruits[0] = "pineapple"

# fruits.append("pineapple") #to add an element at the end of the list
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
#       for reversing alphabetical order first sort then reverse
# fruits.clear()
# print(fruits.index("Mango"))
# print(fruits.count("Mango"))
# fruits.pop() # remove the last elm
# print(fruits)

#       set
vehicles = {"car", "cycle", "motorcylce"}
# print(vehicles)

# print(dir(vehicles))
# print(len(vehicles))
# print("car" in vehicles)

# vehicles.add("airplane")
# vehicles.remove("car")
# vehicles.pop() #randomly remove an element since it unordered (usually remove last elm)
# vehicles.clear()
# print(vehicles)

#           Tuple

students = ("parvaj", "nahid", "ripon", "rajon", "walid", "tanjeem", "imran")
# print(students)
# print(dir(students))
# print("parvaj" in students)
#
# print(students.count("nahid"))
# print(students.index("walid"))

# for student in students:
#     print(student)