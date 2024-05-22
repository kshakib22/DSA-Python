def recursionMethod(n):
  if n < 1:
    print("Number is less than 1")
  else:
    recursionMethod(n - 1)
    print(n)


# Constraints integer and non negative numbers
def factorial(n: int):
  if n == 0:
    return 1
  else:
    return (n * factorial(n - 1))


# Fibonacci that starts from 0. So fibonacci(3) means fourth
# number in the sequence or index 3
# Base case is both 0 and 1. Two base cases should be dealt
# simultaneously
def fibonacci(n: int):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(3))

# Find max element in an array using recursion without max()


def maxTwoNums(num1, num2):
  if num1 >= num2:
    return num1
  else:
    return num2


# First define mathematically
# max(Array, size) = maxNum(last element, max(Array-last element), size -1)
# The type out the return statement
# Finally give the base condition
def maxRecursive(array, size):
  '''
  Takes an array and its size to find its max element
  '''
  if size == 1:
    return array[0]
  return maxTwoNums(array[size - 1], maxRecursive(array, size - 1))


l1 = [1, 6, 2, 4, 3, 72, 23, 4, 3, 65, 12, 3]
print(maxRecursive(l1, len(l1)))


# Mathematically, x^n = x*x^(n-1)
# Add base case
# NOTE this will fail a lot of test cases, especially with large powers (stack overflow). Better approach is Divide and Conquer
def power(x, n):
  '''
  Takes number x and raises it to power n 
  '''
  if n == 0:
    return 1
  elif n < 0:
    return (1 / x) * power(x, n + 1)

  return x * power(x, n - 1)


x, y = 5, -1
print("Value of {} to the power {} is {}".format(x, y, power(x, y)))
