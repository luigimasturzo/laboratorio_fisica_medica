def sign(x):
    """ Print out the sign of the argument x.
    """
    if x > 0:
        return 'Positive'
    elif x == 0:
        return 'Zero'
    else:
        return 'Negative'
 
print(sign(2), sign(0), sign(-2))

