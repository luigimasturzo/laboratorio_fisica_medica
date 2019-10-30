import math
import random
random.seed(1)

# Define the measurements (make sure you do understand the following
# three lines and put in print statements if that is helpful).
# Note you can split long lines with a "\" character
n = 9
m0 = 1.5
q0 = 1.0
xvalues = [i + 1.0 for i in range(n)]
yerrors = [0.05 + 0.02*i for i in range(n)]
yvalues = [m0*x + q0 + random.gauss(0, dy) for \
               x, dy in zip(xvalues, yerrors)]

# Initialize some variables (note we do all at once).
s = sx = sxx = sy = sxy = 0.
# Loop over the data points.
for x, y, dy in zip(xvalues, yvalues, yerrors):
    w = 1./(dy**2)
    s += w
    sx += x*w
    sxx += (x**2)*w
    sy += y*w
    sxy += x*y*w
# Calculate the fit parameters.
D = (sxx*s - sx**2)
m = (sxy*s - sx*sy)/D
sigma_m = math.sqrt(s/D)
q = (sy*sxx - sxy*sx)/D
sigma_q = math.sqrt(sxx/D)

# And here a first example of formatted output.
print('m = %.3f +- %.3f, q = %.3f +- %.3f' % (m, sigma_m, q, sigma_q))
