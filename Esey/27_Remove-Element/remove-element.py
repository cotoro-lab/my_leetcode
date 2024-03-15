# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [num for num in nums if num != val]
        """
        リスト内包記法を分かりやすくした処理
        wk_list = []
        for num in nums:
            if num != val:
                wk_list.append(num)
        nums[:] = wk_list
        """

        """
        一番早かった処理
        while val in nums:
            nums.remove(val)
        """

        return len(nums)

