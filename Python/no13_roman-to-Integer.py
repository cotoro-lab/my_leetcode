class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        s_list = list(s)
        s_pre = ""
        rtn_num = 0
        for s_val in s_list:
            print(roman[s_val])
            rtn_num += int(roman[s_val])
            if (s_val == "V" or s_val == "X") and s_pre == "I":
                rtn_num -= 2

            if (s_val == "L" or s_val == "C") and s_pre == "X":
                rtn_num -= 20

            if (s_val == "D" or s_val == "M") and s_pre == "C":
                rtn_num -= 200

            s_pre = s_val
        return rtn_num
                
