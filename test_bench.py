import univarroot
import numpy
import math
import time
import matplotlib.pyplot as plt
a = -50
b = 100
epsilon = 0.01
width = 0.01
x_vector = numpy.arange(a,b,width)
def fn(x):
    return(math.pow(x,3) - math.pow(x,2) + 4)
t1 = time.clock()
root1 = univarroot.bisection_method(fn,a,b,epsilon,width)
print(root1)
t2 = time.clock()
root2 = univarroot.exhaustive(fn,x_vector)
print(root2)
t3 = time.clock()
print(t2-t1)
print(t3-t2)
fnv = numpy.vectorize(fn)
plt.plot(fnv(x_vector),x_vector)
plt.grid(1)
plt.show()