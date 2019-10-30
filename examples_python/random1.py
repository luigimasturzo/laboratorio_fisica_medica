import random
# Fix the seed to a conventional value for reproducibility.
random.seed(1)

# Extract a random number from a uniform distribution between 0 and 1.
a = random.random()
# Now a gaussian distribution with mean = 10 and sigma = 2.
b = random.gauss(10, 2)
# And, finally, simulate the roll of a die.
c = random.randint(1, 6)
print(a, b, c)
