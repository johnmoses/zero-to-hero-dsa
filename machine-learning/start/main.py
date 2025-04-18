"""
Implement a simple linear regression algorithm from scratch to calculate
the slope, intercept, corellation coeficient, error, and predict fiture values.

Example 1:
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
"""
class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.mean_x = sum(x) / self.n
        self.mean_y = sum(y) / self.n
        self.slope = self.calculate_slope()
        self.intercept = self.calculate_intercept()
        self.correlation_coef = self.calculate_correlation_coef()
        self.error = self.calculate_error()

    def calculate_slope(self):
        numerator = sum((xi - self.mean_x) * (yi - self.mean_y) for xi, yi in zip(self.x, self.y))
        denominator = sum((xi - self.mean_x) ** 2 for xi in self.x)
        return numerator / denominator

    def calculate_intercept(self):
        return self.mean_y - self.slope * self.mean_x

    def calculate_correlation_coef(self):
        numerator = sum((xi - self.mean_x) * (yi - self.mean_y) for xi, yi in zip(self.x, self.y))
        denominator = (sum((xi - self.mean_x) ** 2 for xi in self.x) * sum((yi - self.mean_y) ** 2 for yi in self.y)) ** 0.5
        return numerator / denominator

    def calculate_error(self):
        return sum((yi - (self.slope * xi + self.intercept)) ** 2 for xi, yi in zip(self.x, self.y))

    def predict_y(self, x_value):
        return self.slope * x_value + self.intercept

    def print_results(self):
        print("Slope:", self.slope)
        print("Intercept:", self.intercept)
        print("Correlation Coefficient:", self.correlation_coef)
        print("Error:", self.error)
        print('Prediction at 5:', self.predict_y(5))
        print('Prediction at 10:', self.predict_y(10))
        print('Prediction at 20:', self.predict_y(20))

ln = LinearRegression([5,7,8,7,2,17,2,9,4,11,12,9,6], [99,86,87,88,111,86,103,87,94,78,77,85,86])
ln.print_results()