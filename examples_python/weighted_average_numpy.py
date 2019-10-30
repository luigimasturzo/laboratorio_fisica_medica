import numpy

# Define the measurements (note they are numpy array).
values = numpy.array([1.325, 1.36, 1.32, 1.338, 1.335])
errors = numpy.array([0.012, 0.05, 0.01, 0.005, 0.006])

# And use the numpy facilities to do the actual computation on the fly!
weights = 1./errors**2
average = (values*weights).sum()/weights.sum()
average_err = numpy.sqrt(1./weights.sum())

print(average, average_err)
