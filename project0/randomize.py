import numpy as np

def randomization(n):
    """
    Arg:
        n - is and integer
    
    Returns:
        A - is a randomly generated nx1 array.
    """
    A = np.random.random([n,1])
    return A
    raise NotImplementedError

print(randomization(10))