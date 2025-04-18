/**
 Implement a simple linear regression algorithm from scratch to calculate
the slope, intercept, corellation coeficient, error, and predict fiture values.

Example 1:
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
 */
public class main {
    private double[] x;
    private double[] y;
    private double slope;
    private double intercept;
    private double correlationCoefficient;
    private double error;

    public main(double[] x, double[] y) {
        this.x = x;
        this.y = y;

        calculateRegression();
    }


    private double calculateMean(double[] values) {
        double sum = 0;
        for (double value : values) {
            sum += value;
        }
        return sum / values.length;
    }


    private void calculateRegression() {
        double xMean = calculateMean(x);
        double yMean = calculateMean(y);
        double numerator = 0;
        double denominator = 0;

        for (int i = 0; i < x.length; i++) {
            numerator += (x[i] - xMean) * (y[i] - yMean);
            denominator += Math.pow(x[i] - xMean, 2);
        }


        slope = numerator / denominator;
        intercept = yMean - (slope * xMean);
        calculateCorrelationCoefficient();
        calculateError();
    }


    private void calculateCorrelationCoefficient() {
        double xMean = calculateMean(x);
        double yMean = calculateMean(y);
        double numerator = 0;
        double xDenominator = 0;
        double yDenominator = 0;

        for (int i = 0; i < x.length; i++) {
            numerator += (x[i] - xMean) * (y[i] - yMean);
            xDenominator += Math.pow(x[i] - xMean, 2);
            yDenominator += Math.pow(y[i] - yMean, 2);
        }


        correlationCoefficient = numerator / Math.sqrt(xDenominator * yDenominator);
    }


    private void calculateError() {
        double sumSquaredError = 0;
        for (int i = 0; i < x.length; i++) {
            double predicted = predict(x[i]);
            sumSquaredError += Math.pow(y[i] - predicted, 2);
        }
        error = Math.sqrt(sumSquaredError / x.length);
    }


    public double predict(double xValue) {
        return slope * xValue + intercept;
    }
    public double getSlope() {
        return slope;
    }
    public double getIntercept() {
        return intercept;
    }
    public double getCorrelationCoefficient() {
        return correlationCoefficient;
    }
    public double getError() {
        return error;
    }

    public static void main(String[] args) {
        double[] x = {5,7,8,7,2,17,2,9,4,11,12,9,6};
        double[] y = {99,86,87,88,111,86,103,87,94,78,77,85,86};

        main regression = new main(x, y);

        System.out.println("Slope: " + regression.getSlope());
        System.out.println("Intercept: " + regression.getIntercept());
        System.out.println("Correlation Coefficient: " + regression.getCorrelationCoefficient());
        System.out.println("Error: " + regression.getError());

        double predictedValue5 = regression.predict(5);
        double predictedValue10 = regression.predict(10);
        double predictedValue20 = regression.predict(20);
        System.out.println("Predicted value for 5 = : " + predictedValue5);
        System.out.println("Predicted value for 10 = : " + predictedValue10);
        System.out.println("Predicted value for 20 = : " + predictedValue20);
    }
}

