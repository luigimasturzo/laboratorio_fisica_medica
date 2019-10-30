m = 2**64
a = 6364136223846793005
c = 1442695040888963407
seed = 1

# Set the initial value to the seed.
x = seed

# Generate and print out a few pseudo-random numbers.
for i in range(5):
    x = (a*x + c) % m
    print(float(x)/(m - 1))
