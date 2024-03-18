# 66. Plus One
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        join_digits = int("".join(map(str, digits)))
        rtn_digits = list(map(int, str(join_digits + 1)))
        return rtn_digits