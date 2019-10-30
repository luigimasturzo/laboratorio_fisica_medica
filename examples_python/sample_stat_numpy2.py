import numpy

# Generate a random vector of data (this time we use numpy).
numpy.random.seed(1)
sample = numpy.random.normal(0., 1., 10000)

# Calculate the sample statistics and print out mean and stdev.
mean = numpy.mean(sample)
stdev = numpy.std(sample, ddof = 1)
print(mean, stdev)
