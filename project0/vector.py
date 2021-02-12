import numpy as np

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    if x <= y:
        f=x*y
    else:
        f=x/y
    return f
    raise NotImplementedError

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    return np.vectorize(scalar_function)(x,y)
    raise NotImplementedError

""" print(scalar_function(4,6))

print(scalar_function(6,4)) """

#mynewfunc = np.vectorize(scalar_function)

a = np.random.random([2,3])
b = np.random.random([2,3])

print(a,b)

print(vector_function(a,b))