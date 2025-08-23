// Real World Application - Simple collaborative filtering (C++) simplified

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double cosineSimilarity(const vector<double>& v1, const vector<double>& v2) {
    double dot = 0, norm1 = 0, norm2 = 0;
    for(size_t i = 0; i < v1.size(); i++) {
        dot += v1[i] * v2[i];
        norm1 += v1[i] * v1[i];
        norm2 += v2[i] * v2[i];
    }
    if(norm1 == 0 || norm2 == 0) return 0;
    return dot / (sqrt(norm1) * sqrt(norm2));
}

int main() {
    vector<vector<double>> ratings = {
        {5,3,0,1},
        {4,0,0,1},
        {1,1,0,5},
        {0,0,5,4},
        {0,1,5,4}
    };

    int user = 0;
    vector<pair<int, double>> similarities;

    for(int i = 0; i < (int)ratings.size(); i++) {
        if(i != user) {
            double sim = cosineSimilarity(ratings[user], ratings[i]);
            similarities.emplace_back(i, sim);
        }
    }
    sort(similarities.begin(), similarities.end(),
         [](auto&a, auto&b){ return a.second > b.second; });

    vector<double> weightedRatings(ratings[0].size(), 0);
    double totalSim = 0;
    int topN = 2;
    for(int i = 0; i < topN && i < (int)similarities.size(); i++) {
        int idx = similarities[i].first;
        double sim = similarities[i].second;
        for(size_t j = 0; j < ratings[0].size(); j++) {
            weightedRatings[j] += sim * ratings[idx][j];
        }
        totalSim += sim;
    }
    if(totalSim > 0)
        for(double &r : weightedRatings) r /= totalSim;

    cout << "Recommendations for user " << user << ": ";
    for(size_t i = 0; i < ratings[0].size(); i++) {
        if(ratings[user][i] == 0) {
            cout << "(" << i << ", " << weightedRatings[i] << ") ";
        }
    }
    cout << endl;

    return 0;
}
