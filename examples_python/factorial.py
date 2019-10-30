def factorial(n):
    """ Return the factorial of the argument n.
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n - 1)

print(factorial(0), factorial(1), factorial(5))
