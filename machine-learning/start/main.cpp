/*
Implement a simple linear regression algorithm from scratch to calculate
the slope, intercept, corellation coeficient, error, and predict fiture values.

Example 1:
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
*/
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>

using namespace std;

class LinearRegression {
public:
    double slope;
    double intercept;
    double correlationCoefficient;
    double error;

    LinearRegression(const vector<double>& x, const vector<double>& y) {
        if (x.size() != y.size() || x.empty()) {
            throw invalid_argument("x and y must have the same size and be non-empty");
        }
        calculate(x, y);
    }

    void calculate(const vector<double>& x, const vector<double>& y) {
        double sumX = accumulate(x.begin(), x.end(), 0.0);
        double sumY = accumulate(y.begin(), y.end(), 0.0);
        double sumXY = 0.0;
        double sumX2 = 0.0;
        double sumY2 = 0.0;
        int n = x.size();

        for (int i = 0; i < n; ++i) {
            sumXY += x[i] * y[i];
            sumX2 += x[i] * x[i];
            sumY2 += y[i] * y[i];
        }

        slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
        intercept = (sumY - slope * sumX) / n;

        double rNumerator = n * sumXY - sumX * sumY;
        double rDenominator = sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));
        correlationCoefficient = rNumerator / rDenominator;

        error = 0.0;
        for (int i = 0; i < n; ++i) {
            error += pow(y[i] - (slope * x[i] + intercept), 2);
        }
        error /= n;
    }

    double predict(double x) const {
        return slope * x + intercept;
    }
};

int main() {
    vector<double> x = {5,7,8,7,2,17,2,9,4,11,12,9,6};
    vector<double> y = {99,86,87,88,111,86,103,87,94,78,77,85,86};

    LinearRegression model(x, y);
    cout << "Slope: " << model.slope << endl;
    cout << "Intercept: " << model.intercept << endl;
    cout << "Correlation Coefficient: " << model.correlationCoefficient << endl;
    cout << "Error: " << model.error << endl;
    cout << "Predicted value for x = 5: " << model.predict(5) << endl;
    cout << "Predicted value for x = 10: " << model.predict(10) << endl;
    cout << "Predicted value for x = 20: " << model.predict(20) << endl;

    return 0;
}