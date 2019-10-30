import pylab
import numpy
from scipy.optimize import curve_fit

def fit_function(x, omega,b):
    """ Definition of the fit function.
    """


    return pylab.exp(omega*x)+b

# Load the data from the file.
v, i, di = pylab.loadtxt('cristian.txt',skiprows=6, unpack = True)

# Do the fit.
initial_values = (0.1,0.1)
pars, covm = curve_fit(fit_function, v, i, initial_values, di)
omega0 = pars[0]
b=pars[1]

# Plot the data points and the fit function.
pylab.rc('font', size = 18)
pylab.title('Law of motion fit', y = 1.02)
pylab.xlabel('t [s]')
pylab.ylabel('s [m]', labelpad = 5)
pylab.xlim(0, 20)
pylab.ylim(-1.5, 1.5)
pylab.grid(color = 'gray')
x = numpy.linspace(-5, 4, 200)
y = fit_function(x, omega0,b)
pylab.errorbar(v, i, di, linestyle = '', color = 'black', marker = 'o')
pylab.plot(x, y, color = 'black')

# Save the plot to a pdf file for later use (maybe in a writeup?).
#pylab.savefig('fit_initial_val_fitplot.pdf')

# Finally: show the plot on the screen.
pylab.show()
