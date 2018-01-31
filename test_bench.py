import math
def fn(x):
    return(x+1)


def test(fn,x,y):
    return(fn(x)/y)
import univarroot

def Rd1_fn(fn,x,width): #This is the computation of first order right hand derivative
    derivative = fn(x+width)-fn(x)
    derivative = derivative/width
    return(derivative)
a=-3
b=2
epsilon = 0.01
width =0.0001

import numpy
alpha = (a+b)/2
x_vector = numpy.array(a,b,width)
# while(1):
#
#     if((Rd1_fn(fn,a,width)*Rd1_fn(fn,alpha,width) < 0)):
#         b = alpha
#     else:
#         a = alpha
#
#     print(Rd1_fn(fn, a, width))
#     print (Rd1_fn(fn, alpha, width))
#     print(alpha)
#     print(a)
#     print(b)
# print(a)

# root = univarroot.bisection_method(poly,-2,2,0.001,0.00001)
# root = test(poly,2,0.1)
# print(root)