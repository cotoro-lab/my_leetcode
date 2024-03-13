// Problem 1005. 
// Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

public class Solution {
    public int LargestSumAfterKNegations(int[] nums, int k) {
        int rtn = 0;

        for(int i = 0; i < k; i++){
        Array.Sort(nums);
        nums[0] = nums[0] * -1;
        }

        foreach(int num in nums){
            rtn = rtn + num;
        }
        
        return rtn;
    }
}
