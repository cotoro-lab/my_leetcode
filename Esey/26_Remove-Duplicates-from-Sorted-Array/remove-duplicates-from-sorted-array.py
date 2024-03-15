# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        wk_items = []

        for i in range(0, len(nums)):
            if i == 0 or nums[i] != wk_items[len(wk_items) - 1]:
                wk_items.append(nums[i])

        nums[:] = wk_items
        return len(nums)