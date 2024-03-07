//https://leetcode.com/problems/two-sum/

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int nums_len = nums.Length;
        int[] rtn = new int[2];

        for(int i = 0 ; i < nums_len; i++){
            int n = 0;
            int wk_num = nums[i];

            foreach(int num in nums){
                if(i != n){
                    if(target == wk_num + num){
                        rtn[0] = i;
                        rtn[1] = n;
                    }
                }
                n++;
            }
        }
        return rtn;
    }
}
