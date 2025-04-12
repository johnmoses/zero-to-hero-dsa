"""  
Write a simple neural network lineare regression algorithm from scratch
"""

import numpy as np

def init_weights(input_size):
    """Initialize random weights and bias"""
    weights = np.random.randn(input_size, 1) * 0.01
    bias = np.zeros((1, 1))
    return weights, bias

def forward_prop(X, weights, bias):
    """Forward propagation step"""
    return np.dot(X, weights) + bias

def compute_cost(y_hat, y):
    """Compute the cost function"""
    m = y.shape[0]
    cost = (1 / (2 * m)) * np.sum(np.square(y_hat - y))
    return cost

def back_prop(X, y, y_hat):
    """Back propagation step"""
    m = X.shape[0]
    dw = (1 / m) * np.dot(X.T, (y_hat - y))
    db = (1 / m) * np.sum(y_hat - y)
    return dw, db

def update_params(weights, bias, dw, db, learning_rate):
    """Update the weights and bias"""
    weights = weights - learning_rate * dw
    bias = bias - learning_rate * db
    return weights, bias

def train(X, y, learning_rate, num_iterations):
    """Train the model"""
    input_size = X.shape[1]
    weights, bias = init_weights(input_size)
    costs = []
    for i in range(num_iterations):
        y_hat = forward_prop(X, weights, bias)
        cost = compute_cost(y_hat, y)
        dw, db = back_prop(X, y, y_hat)
        weights, bias = update_params(weights, bias, dw, db, learning_rate)
        costs.append(cost)
        if i % 100 == 0:
            print(f"Cost after iteration {i}: {cost}")
    return weights, bias, costs

def predict(X, weights, bias):
    """Predict the output"""
    y_hat = forward_prop(X, weights, bias)
    return y_hat

# Example usage
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([[2], [4], [6], [8], [10]])
learning_rate = 0.01
num_iterations = 1000
weights, bias, costs = train(X, y, learning_rate, num_iterations)
y_hat = predict(X, weights, bias)
print(f"Predicted values: {y_hat}")
print(f"Actual values: {y}")
