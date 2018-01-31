# what you see here is the module for solving roots
#     This includes
#         1. exhaustive()
#         2. newtonraphson()

# This is the function to solve for the roots of the function using the exhaustive search method, it takes care for the derivative of the function
def exhaustive(fn,x_vector):
    func_vector = []
    for i in range(0,len(x_vector)):
        d = fn(x_vector[i])
        func_vector.append(d)
    nroots = 0
    last_point = 0
    roots = []
    for i in range(1,len(x_vector)):
        if (func_vector[i] * func_vector[last_point] < 0 ):
            nroots = nroots +1
            last_point = i
            roots.append((x_vector[i]) + (x_vector[i+1] - x_vector[i])/2 )
    dfunc_vector = []
    for i in range(0,len(x_vector)-1):
        derivative = func_vector[i+1] - func_vector[i]
        derivative = derivative/(x_vector[i+1] - x_vector[i])
        dfunc_vector.append(derivative)
    dnroots = 0
    dlast_point = 0
    droots = []
    for i in range(1,len(dfunc_vector)):
        if (dfunc_vector[i] * dfunc_vector[dlast_point]< 0 ):
            dlast_point = i
            dnroots = dnroots +1
            droots.append(i)
    tolerance = 0.01
    new_nroot = 0
    if(nroots != dnroots):
        for i in range(0,len(droots)):
            if(abs(func_vector[droots[i]]) < tolerance):
                new_nroot = new_nroot +1
                roots.append(x_vector[droots[i]])
    return(roots)


def d1_fn(fn,x,width): #This is the computation of first order derivative
    derivative = fn(x+width)-fn(x-width)
    derivative = derivative/2.0/width
    return(derivative)

def d2_fn(fn,x,width): #This is the computation of second order derivative
    derivative = fn(x+width)- 2*fn(x) +fn(x-width)
    derivative = derivative/(width*width)
    return(derivative)

def differentiability(fn,x,width,tolerance):
    if abs((Ld1_fn(fn,x,width) - Ld1_fn(fn,x,width) )) < tolerance :
        return(1)
    else: return(0)

def bisection_method(fn,a,b,epsilon,width):
    alpha = (a+b)/2
    i = 0
    if ((d1_fn(fn, a, width) * d1_fn(fn, alpha, width)) < 0 & (fn(a) * fn(b) > 0)):
        while (abs(a - b) > epsilon):
            i = i + 1
            alpha = (a + b) / 2.0
            if ((d1_fn(fn, a, width) * d1_fn(fn, alpha, width)) < 0):
                b = alpha
            else:
                a = alpha
            if (abs(a - b) < epsilon):
                break
        root = alpha
    if ((d1_fn(fn, a, width) * d1_fn(fn, alpha, width)) > 0 & (fn(a) * fn(b) < 0)):
        while (abs(a - b) > epsilon):
            i = i + 1
            alpha = (a + b) / 2.0
            if ((fn(a) * fn(b) < 0)):
                b = alpha
            else:
                a = alpha
            if (abs(a - b) < epsilon):
                break
        root = alpha
    return(root)


def newtonraphson(fn,xo,epsilon,width):
    while(abs(fn(xo)) > epsilon):
        xn = xo - ((d1_fn(fn,xo,width))/d2_fn(fn,xo,width))
        xo = xn
    return(xo)
# # def gradient(func_vector):
# # def positive_definite():
