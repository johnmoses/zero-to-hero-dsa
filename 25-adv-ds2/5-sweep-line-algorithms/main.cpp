// Sweep Line Algorithms - C++ example (Counting overlapping intervals)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countOverlaps(vector<pair<int,int>>& intervals) {
    vector<pair<int,int>> events;
    for(auto &interval : intervals) {
        events.push_back({interval.first, 1});  // Interval start
        events.push_back({interval.second, -1}); // Interval end
    }

    sort(events.begin(), events.end());

    int active = 0, maxOverlaps = 0;
    for(auto &event : events) {
        active += event.second;
        maxOverlaps = max(maxOverlaps, active);
    }
    return maxOverlaps;
}

int main() {
    vector<pair<int,int>> intervals = {{1,3}, {2,5}, {4,6}, {7,8}};
    cout << countOverlaps(intervals) << endl;  // Output: 3
    return 0;
}
