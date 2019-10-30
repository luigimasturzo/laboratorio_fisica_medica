import numpy


def straight_line(x, m, q):
    """ Definition of a simple straight line of the form y = m*x + q.
    """
    return m*x + q


# Create an array of number, from 0 to 10 in 5 steps.
x0 = numpy.linspace(0., 10., 5)
# Set the straight-line parameters.
m0 = 2.
q0 = 1.

# Print the values of the independent and dependent variable.
print(x0)
print(straight_line(x0, m0, q0))
