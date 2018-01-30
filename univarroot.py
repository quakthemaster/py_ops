# what you see here is the module for solving roots
#     This includes
#         1. exhaustive()
#         2. newtonraphson()

# This is the function to solve for the roots of the function using the exhaustive search method, it takes care for the derivative of the function
def exhaustive(func_vector,x_vector):
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

# def bisection(func_vector,x_vector,a,b):
#     # just checking if git works or not
#     print('How are you')
# def newtonraphson(func_vector,x_vector,a,b):
# def gradient(func_vector):
# def positive_definite():
