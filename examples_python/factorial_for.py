def factorial(n):
    """ Return the factorial of the argument n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(0), factorial(1), factorial(5))
