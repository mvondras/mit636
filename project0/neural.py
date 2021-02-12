import numpy as np

def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
  

    weights=weights.transpose()

    #print(weights, "\n\n")
  
    out=np.tanh(np.matmul(weights, inputs))
    return out
    raise NotImplementedError


i= np.random.random([2,1])
w= np.random.random([2,1])

print(i,w)

print("\n\n",neural_network(i,w))