# Lambda function = A small anonymous function for a one time use (throw away function)
#                     They take any number of arguments, but have only 1 expression
#                      Helps keep the namespace clear and is useful with higher order functions
#                       'sort()', 'map()', 'filter()', 'reduce()'
#                           lambda parameters: expression

# double = lambda x:x*2
# add = lambda x, y : x + y
# max_value = lambda x,y : x if x>y else y
# fullName = lambda first, last: first + " " + last
# is_even = lambda x: x % 2 == 0
# age_check = lambda age: True if age >= 18 else False

# print(double(3))
# print(add(2,3))
# print(max_value(5,3))
# print(fullName("parvaj", "Mosharof"))
# print(is_even(46))
# print(age_check(3))