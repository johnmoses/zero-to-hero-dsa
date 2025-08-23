# AI Math Fundamentals - Python example (Matrix multiplication and gradient computation)

import numpy as np

# Matrix multiplication example
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)
print("Matrix multiplication result:\n", C)

# Gradient descent step example
def gradient_descent_step(x, grad, learning_rate=0.1):
    return x - learning_rate * grad

x = 5.0
grad = 2 * x  # derivative of x^2
x_new = gradient_descent_step(x, grad)
print("Updated x after gradient descent step:", x_new)
