import univarroot
import numpy
import math
import time
import matplotlib.pyplot as plt
a = -2
b = 3
epsilon = 0.01
width = 0.01
x_vector = numpy.arange(a,b,width)
def fn(x):
    return(math.pow(x,2))
t1 = time.clock()
root1 = univarroot.bisection_method(fn,a,b,epsilon,width)
print(root1)
t2 = time.clock()
root2 = univarroot.exhaustive(fn,x_vector)
print(root2)
t3 = time.clock()
xo =2
while (1):
    xn = xo - ((univarroot.d1_fn(fn, xo, width)) / univarroot.d2_fn(fn, xo, width))
    print(xn)
    xo = xn
    root3 = xo
    if(abs(fn(xo))<epsilon):
        break
print(xo)
print(root3)
t4 = time.clock()
print(t2-t1)
print(t3-t2)
print(t4-t3)
fnv = numpy.vectorize(fn)
plt.plot(x_vector,fnv(x_vector))
plt.grid(1)
plt.show()