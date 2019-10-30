import math

def get_stat(sample):
    """ Return the sample mean and variance for a list of values.

    This is done in two separate steps, i.e., we calculate the mean
    first, then the average.
    """
    # Calculate the mean (do not initialize mean as an integer!).
    mean = 0.
    for value in sample:
        mean += value
    mean /= len(sample)
    # Calculate the variance
    variance = 0.
    for value in sample:
        variance += (value - mean)**2.0
    variance /= len(sample) - 1
    # Return the two numbers.
    return mean, variance


# Generate a random vector of data.
import random
random.seed(1)
sample = [random.gauss(0, 1) for i in range(10000)]

# Calculate the sample statistics and print out mean and stdev.
mean, variance = get_stat(sample)
print(mean, math.sqrt(variance))
