class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        str_xx = str_x[::-1]
        return str_x == str_xx
        
