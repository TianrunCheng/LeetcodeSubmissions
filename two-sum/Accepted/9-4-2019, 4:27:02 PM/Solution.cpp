// https://leetcode.com/problems/two-sum

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res = {};
        for (int i=0;i<=(nums.size()-2);++i){
            for(int j=(i+1);j<=(nums.size()-1);++j){
                if (nums[i]+nums[j]==target){
                    res.push_back(i);
                    res.push_back(j);
                    return res;
                }
            }
        }
        return res;
    }
};