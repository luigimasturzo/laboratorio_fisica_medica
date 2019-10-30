def factorial(n):
    """ Return the factorial of the argument n.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial(0), factorial(1), factorial(5))
