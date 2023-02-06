// Problem 416. 
// Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/description/

public class Solution {
    public bool CanPartition(int[] nums) {
        bool rtn = false;
        int wk_sum = nums.Sum();

        if(wk_sum % 2 != 0){
            return rtn;
        }

        Array.Sort(nums);
        int wk_int = 0;
        foreach(int i in nums){
            wk_int = wk_int + i;
            if(wk_int == wk_sum / 2){
                rtn = true;
                return rtn;
            }
        }

        return rtn;
    }
}