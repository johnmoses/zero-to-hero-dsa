/*
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
*/
#include <iostream>
#include <vector>
using namespace std;

int search(vector<int>& nums, int target) {
        int l=0,r=nums.size()-1;
        while(l<=r){
            int mid=l+(r-l)/2;
            if(nums[mid]==target)
                return mid;
            else if(nums[mid]<target)
                l=mid+1;
            else
                r=mid-1;
        }
        return -1;
    }

int main(){
    vector<int> nums={-1,0,3,5,9,12};
    int target=9;
    cout<<search(nums,target);
    return 0;
}