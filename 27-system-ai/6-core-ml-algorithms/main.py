# Core ML Algorithms - Python example (Linear Regression)

import numpy as np

class LinearRegression:
    def __init__(self):
        self.coeff = None
        self.intercept = None

    def fit(self, X, y):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
        self.intercept = theta_best
        self.coeff = theta_best[1:]

    def predict(self, X):
        return X.dot(self.coeff) + self.intercept

if __name__ == "__main__":
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([3, 6, 9, 12, 15])
    model = LinearRegression()
    model.fit(X, y)
    preds = model.predict(np.array([[6], ]))
    print("Predictions:", preds)
