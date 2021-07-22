// https://leetcode.com/problems/set-mismatch

class Solution {
    public int[] findErrorNums(int[] nums) {
        // sort nums first, duplicates will be shown by two consecutive same number
        // the missing value will be obvious in its >1 gap between 
        Arrays.sort(nums);
        int dup = -1, missing = 1;
        for(int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1])
                dup = nums[i];
            else if (nums[i] > nums[i-1] + 1)
                missing = nums[i-1] + 1;
        }
        return new int[] {dup, nums[nums.length - 1] != nums.length ? nums.length : missing}
    }
}