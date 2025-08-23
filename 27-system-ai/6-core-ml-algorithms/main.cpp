// Core ML Algorithms - C++ example (Simple Linear Regression)

#include <iostream>
#include <vector>

using namespace std;

class LinearRegression {
public:
    double coeff = 0;
    double intercept = 0;

    void fit(const vector<double>& X, const vector<double>& y) {
        int n = X.size();
        double sum_x = 0, sum_y = 0, sum_xx = 0, sum_xy = 0;
        for (int i = 0; i < n; ++i) {
            sum_x += X[i];
            sum_y += y[i];
            sum_xx += X[i] * X[i];
            sum_xy += X[i] * y[i];
        }
        coeff = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x);
        intercept = (sum_y - coeff * sum_x) / n;
    }

    double predict(double x) {
        return coeff * x + intercept;
    }
};

int main() {
    vector<double> X = {1, 2, 3, 4, 5};
    vector<double> y = {3, 6, 9, 12, 15};

    LinearRegression model;
    model.fit(X, y);

    cout << "Predictions: " << model.predict(6) << " " << model.predict(7) << endl;
    return 0;
}
