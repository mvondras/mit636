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

print(scalar_function(4,6))

print(scalar_function(6,4))