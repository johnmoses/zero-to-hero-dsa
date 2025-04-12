/*
Template 1

Example 1:
    
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
*/
#include <iostream>
#include <vector>

using namespace std;

int binarySearch(vector<int>& nums, int target){
  if(nums.size() == 0)
    return -1;

  int left = 0, right = nums.size() - 1;
  while(left <= right){
    // Prevent (left + right) overflow
    int mid = left + (right - left) / 2;
    if(nums[mid] == target){ return mid; }
    else if(nums[mid] < target) { left = mid + 1; }
    else { right = mid - 1; }
  }

  // End Condition: left > right
  return -1;
}

int main(){
    vector<int> nums = {-1,0,3,5,9,12};
    int target = 9;
    int index = binarySearch(nums, target);
    cout << index << endl;
    return 0;
}