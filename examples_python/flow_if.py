def absvalue(x):
    """ Poor man's implementation of the absolute value.

    python provides an abs() function that does the job (and does
    it better, too), so there is no need to reinvent the wheel, here.
    """
    if x >= 0:
        return x
    else:
        return -x

# Test that it actually works.
print(absvalue(2.0), absvalue(0.0), absvalue(-2.0))

