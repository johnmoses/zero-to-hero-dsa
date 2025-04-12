"""
Implement a simple linear regression algorithm from scratch

Sample Inputs:
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]

"""
def simple_linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum([i**2 for i in x])
    sum_xy = sum([i*j for i, j in zip(x, y)])

    # Calculate the slope (w1)
    w1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)

    # Calculate the intercept (w0)
    w0 = (sum_y - w1 * sum_x) / n

    return w0, w1

print(simple_linear_regression([1, 2, 3, 4, 5], [2, 4, 5, 4, 5]))
