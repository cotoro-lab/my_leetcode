// https://leetcode.com/problems/shuffle-the-array/

public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        var rtnList = new List<int>();
        
        for(int x = 0; x < n; x++){
            int y = x + n;
            rtnList.Add(nums[x]);
            rtnList.Add(nums[y]);
        }

        return rtnList.ToArray();
    }
}
