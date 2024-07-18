"""

Concept 1 closure

"""


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


var = make_counter()

# is var a function now?
print(var())
print(var())


"""

Concept 2 map

Takes (function, iterable) and applies the function to all the items in iterable
and returns the modified iterable
"""


def double(x):
    return 2 * x


l1 = [12, 13, 14, 15, 16]

# map returns a map object even though it takes a specific iterable
l2 = list(map(double, l1))
print(l2)


"""

Concept 3 filter

Takes (function, iterable) and filters the original iterable items for which the 
function returns True
"""


def isEven(n):
    return n % 2 == 0


ll1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(isEven, ll1))
print(evens)


"""

Concept 4 reduce

Takes (function, iterable) and cumulatively applies the function to iterables in order left->right
Takes exactly two input values
This means addition = cumulative sum
multiply = factorial
"""
from functools import reduce


def multiply(x, y):
    return x * y


lll3 = [1, 2, 3, 4]
product = reduce(multiply, lll3)

print(product)


"""
Combining things

"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = list(filter(lambda n: n % 2 == 0, nums))
squared_evens = list(map(lambda n: n**2, even_nums))

print(squared_evens)

sum_of_squares = reduce(lambda x, y: x + y, squared_evens)
print(sum_of_squares)
