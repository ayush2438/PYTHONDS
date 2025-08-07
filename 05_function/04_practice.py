# Pure Function
def pure_add(a, b):
    return a + b

# Global variable for impure function
counter = 0

def impure_increment():
    global counter
    counter += 1
    return counter

# Recursive factorial function
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Lambda function with map()
def square_list(nums):
    return list(map(lambda x: x**2, nums))
