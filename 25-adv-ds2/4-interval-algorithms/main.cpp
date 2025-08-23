// Interval Algorithms - C++ example (Merge Intervals)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int,int>> mergeIntervals(vector<pair<int,int>>& intervals) {
    if(intervals.empty()) return {};
    sort(intervals.begin(), intervals.end());
    vector<pair<int,int>> merged;
    merged.push_back(intervals[0]);

    for(int i = 1; i < intervals.size(); ++i) {
        if(intervals[i].first <= merged.back().second) {
            merged.back().second = max(merged.back().second, intervals[i].second);
        } else {
            merged.push_back(intervals[i]);
        }
    }
    return merged;
}

int main() {
    vector<pair<int,int>> intervals = {{1,3}, {2,6}, {8,10}, {15,18}};
    vector<pair<int,int>> merged = mergeIntervals(intervals);
    for(auto &interval : merged) {
        cout << "(" << interval.first << ", " << interval.second << ") ";
    }
    cout << endl;  // Output: (1, 6) (8, 10) (15, 18) 
    return 0;
}
