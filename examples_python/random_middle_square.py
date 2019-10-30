# Implementation of a toy base 10 middle-square generator (Von Neumann, 1946),
# generating two-digits "random" numbers (between 0 and 99).

# Define the seed.
x = 81
print(x)

# Generate 10 numbers.
for i in range(10):
    x = (x**2 // 10) % 100
    print(x)
