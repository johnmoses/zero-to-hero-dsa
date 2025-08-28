// Core ML Algorithms - Java example (Simple Linear Regression)

class Main {
    static class LinearRegression {
        double coeff = 0;
        double intercept = 0;

        public void fit(double[] X, double[] y) {
            int n = X.length;
            double sumX = 0, sumY = 0, sumXX = 0, sumXY = 0;
            for (int i = 0; i < n; i++) {
                sumX += X[i];
                sumY += y[i];
                sumXX += X[i] * X[i];
                sumXY += X[i] * y[i];
            }
            coeff = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
            intercept = (sumY - coeff * sumX) / n;
        }

        public double predict(double x) {
            return coeff * x + intercept;
        }
    }

    public static void main(String[] args) {
        double[] X = {1, 2, 3, 4, 5};
        double[] y = {3, 6, 9, 12, 15};

        LinearRegression model = new LinearRegression();
        model.fit(X, y);

        System.out.println("Predictions: " + model.predict(6) + " " + model.predict(7));
    }
}
