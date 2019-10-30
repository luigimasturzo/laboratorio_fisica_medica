import math

# Define the measurements.
values = [1.325, 1.36, 1.32, 1.338, 1.335]
errors = [0.012, 0.05, 0.01, 0.005, 0.006]

# Initialize a couple of variables (mind that they only represent what
# their name suggest at the end of the program---particularly
# average_err is used in the loop to accumulate the sum of weights).
average = 0.
average_err = 0.

# Note the zip function, that allows to loop over multiple lists
# simultaneously.
for value, error in zip(values, errors):
    weight = 1./(error**2)
    average += weight*value
    average_err += weight
average /= average_err
average_err = math.sqrt(1./average_err)

print(average, average_err)

