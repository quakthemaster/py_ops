# what you see here is the module for solving roots
#     This includes
#         1. exhaustive()
#         2. newtonraphson()

# This is the function to solve for the roots of the function using the exhaustive search method, it takes care for the derivative of the function
# def exhaustive(func_vector,x_vector):
#     nroots = 0
#     last_point = 0
#     roots = []
#     for i in range(1,len(x_vector)):
#         if (func_vector[i] * func_vector[last_point] < 0 ):
#             nroots = nroots +1
#             last_point = i
#             roots.append((x_vector[i]) + (x_vector[i+1] - x_vector[i])/2 )
#     dfunc_vector = []
#     for i in range(0,len(x_vector)-1):
#         derivative = func_vector[i+1] - func_vector[i]
#         derivative = derivative/(x_vector[i+1] - x_vector[i])
#         dfunc_vector.append(derivative)
#     dnroots = 0
#     dlast_point = 0
#     droots = []
#     for i in range(1,len(dfunc_vector)):
#         if (dfunc_vector[i] * dfunc_vector[dlast_point]< 0 ):
#             dlast_point = i
#             dnroots = dnroots +1
#             droots.append(i)
#     tolerance = 0.01
#     new_nroot = 0
#     if(nroots != dnroots):
#         for i in range(0,len(droots)):
#             if(abs(func_vector[droots[i]]) < tolerance):
#                 new_nroot = new_nroot +1
#                 roots.append(x_vector[droots[i]])
#     return(roots)
# def positionofx(x_vector,x,epsilon): #To find the postition of an element in the given list
#     for i in range(0,len(x_vector)):
#         if( abs(x_vector[i] - x) < epsilon):
#             return(i)

def Rd1_fn(fn,x,width): #This is the computation of first order right hand derivative
    derivative = fn(x+width)-fn(x)
    derivative = derivative/width
    return(derivative)

def Ld1_fn(fn,x,width): #This is the computation of first order left hand derivative
    derivative = fn(x)-fn(x-width)
    derivative = derivative/width
    return(derivative)

def differentiability(fn,x,width,tolerance):
    if abs((Ld1_fn(fn,x,width) - Ld1_fn(fn,x,width) )) < tolerance :
        return(1)
    else: return(0)

def bisection_method(fn,a,b,epsilon,width):
    alpha = (a+b)/2
    while(abs(a-b)> epsilon):
        if((Rd1_fn(fn,a,width)*Rd1_fn(fn,alpha,width))):
            b = alpha
        else:
            a = aplha
    return(a)

# def bisection(func_vector,x_vector,a,b,epsilon):
#     alpha = (a+b)/2
#
#    # def newtonraphson(func_vector,x_vector,a,b):
# # def gradient(func_vector):
# # def positive_definite():
