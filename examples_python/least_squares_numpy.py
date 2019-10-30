import numpy
import math
import random
random.seed(1)

# Define the measurements (this is identical to the plain example).
n = 9
m0 = 1.5
q0 = 1.0
xvalues = [i + 1.0 for i in range(n)]
yerrors = [0.05 + 0.02*i for i in range(n)]
yvalues = [m0*x + q0 + random.gauss(0, dy) for \
               x, dy in zip(xvalues, yerrors)]

# Convert the measurements into numpy arrays.
x = numpy.array(xvalues)
y = numpy.array(yvalues)
dy = numpy.array(yerrors)

# Do the actual computation.
w = 1./(dy**2)
s = w.sum()
sx = (x*w).sum()
sxx = ((x**2)*w).sum()
sy = (y*w).sum()
sxy = (x*y*w).sum()
# Calculate the fit parameters.
D = (sxx*s - sx**2)
m = (sxy*s - sx*sy)/D
sigma_m = math.sqrt(s/D)
q = (sy*sxx - sxy*sx)/D
sigma_q = math.sqrt(sxx/D)

# And here a first example of formatted output.
print('m = %.3f +- %.3f, q = %.3f +- %.3f' % (m, sigma_m, q, sigma_q))
