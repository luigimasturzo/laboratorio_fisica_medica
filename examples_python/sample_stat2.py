import math

def get_stat(sample):
    """ Return the sample mean and variance for a list of values.

    This is done in a single loop.
    """
    # Again: do not initialize mean as an integer!
    mean = 0.
    variance = 0.
    n = len(sample)
    for value in sample:
        mean += value
        variance += value**2.0
    mean /= n
    variance = (variance - n*mean**2.0)/(n - 1)
    return mean, variance


# Generate a random vector of data.
import random
random.seed(1)
sample = [random.gauss(0, 1) for i in range(10000)]

# Calculate the sample statistics and print out mean and stdev.
mean, variance = get_stat(sample)
print(mean, math.sqrt(variance))
