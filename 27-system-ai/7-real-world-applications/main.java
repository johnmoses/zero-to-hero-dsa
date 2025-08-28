// Real World Application - Simple collaborative filtering (Java)

import java.util.*;

class Main {
    public static double cosineSimilarity(double[] v1, double[] v2) {
        double dot = 0, norm1 = 0, norm2 = 0;
        for (int i = 0; i < v1.length; i++) {
            dot += v1[i] * v2[i];
            norm1 += v1[i] * v1[i];
            norm2 += v2[i] * v2[i];
        }
        if (norm1 == 0 || norm2 == 0) return 0;
        return dot / (Math.sqrt(norm1) * Math.sqrt(norm2));
    }

    public static List<int[]> recommend(int userIdx, double[][] ratings, int topN) {
        List<int[]> recommendations = new ArrayList<>();
        double[] userRatings = ratings[userIdx];
        List<double[]> sims = new ArrayList<>();
        for (int i = 0; i < ratings.length; i++) {
            if (i != userIdx) {
                double sim = cosineSimilarity(userRatings, ratings[i]);
                sims.add(new double[]{i, sim});
            }
        }
        sims.sort((a, b) -> Double.compare(b[1], a[1]));

        double[] weightedRatings = new double[ratings.length];
        double totalSim = 0;
        for (int i = 0; i < Math.min(topN, sims.size()); i++) {
            int idx = (int) sims.get(i)[0];
            double sim = sims.get(i)[1];
            for (int j = 0; j < ratings.length; j++) {
                weightedRatings[j] += sim * ratings[idx][j];
            }
            totalSim += sim;
        }
        if (totalSim > 0) {
            for (int i = 0; i < weightedRatings.length; i++) {
                weightedRatings[i] /= totalSim;
            }
        }

        for (int i = 0; i < weightedRatings.length; i++) {
            if (userRatings[i] == 0) {
                recommendations.add(new int[]{i, (int)(weightedRatings[i] * 1000)}); // scaled score
            }
        }
        recommendations.sort((a, b) -> Integer.compare(b[1], a[1]));
        return recommendations;
    }

    public static void main(String[] args) {
        double[][] ratings = {
            {5, 3, 0, 1},
            {4, 0, 0, 1},
            {1, 1, 0, 5},
            {0, 0, 5, 4},
            {0, 1, 5, 4}
        };
        int user = 0;
        List<int[]> recs = recommend(user, ratings, 2);
        System.out.println("Recommendations for user " + user + ":");
        for (int[] rec : recs) {
            System.out.println("Item " + rec[0] + ", score: " + rec);
        }
    }
}
