import pylab
from scipy.optimize import curve_fit

def fit_function(x, omega):
    """ Definition of the fit function.
    """
    return pylab.sin(omega*x)

# Load the data from the file.
t, s, ds = pylab.loadtxt('data/fit_initial_val.txt', unpack = True)

# Pick a few different initial values and fit.
for initial_values in [(0.8,), (1.2,), (1.5,), (2.0,)]:
    pars, covm = curve_fit(fit_function, t, s, initial_values, ds)
    print(initial_values[0], pars[0])
