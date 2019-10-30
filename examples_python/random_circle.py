import pylab
import numpy

N = 1000
r = 0.5 

x = numpy.random.uniform(-r, r, N)
y = numpy.random.uniform(-r, r, N)

fig = pylab.figure()
ax = fig.add_subplot(111)
pylab.rc('font', size = 18)
ax.set_aspect('equal')
pylab.xlabel('x [m]')
pylab.ylabel('y [m]')
pylab.xlim(-r, r)
pylab.ylim(-r, r)
pylab.plot(x, y, linestyle = '', marker = 'o', axes = ax, color = 'black')
circ = pylab.Circle((0, 0), r, fill = False)
ax.add_patch(circ)

n_c = sum((x**2 + y**2) < r**2)
pi = 4.0*n_c/N
print(n_c, N, pi)

pylab.savefig('random_circle.pdf')
pylab.show()
