import pylab
import numpy
from scipy.optimize import curve_fit

def fit_function(x, omega):
    """ Definition of the fit function.
    """
    return pylab.sin(omega*x)

# Load the data from the file.
t, s, ds = pylab.loadtxt('data/fit_initial_val.txt', unpack = True)

# Define a grid and calculate the values of the chisquare on the grid
# (note we are not fitting, here).
omega_grid = numpy.linspace(0, 10, 500)
chi2_values = []
for omega in omega_grid:
    chi2 = (((s - fit_function(t, omega))/ds)**2).sum()
    chi2_values.append(chi2)

# Make a plot of the chisquare as a function of omega.
pylab.rc('font', size = 18)
pylab.title('Chisquare scan', y = 1.02)
pylab.xlabel('omega [1/s]')
pylab.ylabel('chisquare', labelpad = 0)
pylab.grid(color = 'gray')
pylab.plot(omega_grid, chi2_values, color = 'black')

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('fit_initial_val_chi2.pdf')

# Finally: show the plot on the screen.
pylab.show()
