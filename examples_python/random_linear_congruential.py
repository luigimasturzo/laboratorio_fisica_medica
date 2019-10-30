# Implementation of a toy linear congruential generator, generating
# two-digits "random" numbers (between 0 and 99).

# Define the seed and the other stuff.
x = 81
a = 11
c = 3
m = 73
print(x)

# Generate 10 numbers.
for i in range(10):
    x = (a*x + c) % m
    print(x)
