""" 
Implement a knn classifier algorithm from scratch

Sample Inputs:
    
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 1, 1, 1])
"""
import numpy as np

def euclidean_distance(x1, x2):
    """Calculate euclidean distance between two points"""
    return np.sqrt(np.sum((x1 - x2) ** 2))

def initialize_centroids(X, k):
    """Randomly initialize k centroids"""
    n_samples = X.shape[0]
    indices = np.random.choice(n_samples, k, replace=False)



