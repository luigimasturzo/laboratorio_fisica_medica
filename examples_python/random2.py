import random
random.seed(1)

# Fill a list with random numbers from a uniform pdf between 0 and 1.
l = [random.random() for i in range(3)]
print(l)
