import numpy

def get_stat(sample):
    """ Return the sample mean and variance for a list of values.

    Note the input argument must be a numpy array.
    """
    mean = sample.sum()
    variance = (sample**2).sum()
    n = len(sample)
    mean /= n
    variance = (variance - n*mean**2.0)/(n - 1)
    return mean, variance


# Generate a random vector of data (this time we use numpy).
numpy.random.seed(1)
sample = numpy.random.normal(0., 1., 10000)

# Calculate the sample statistics and print out mean and stdev.
mean, variance = get_stat(sample)
print(mean, numpy.sqrt(variance))
