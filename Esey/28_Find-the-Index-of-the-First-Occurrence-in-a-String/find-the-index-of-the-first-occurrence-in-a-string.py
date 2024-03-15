# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hs_list = list(haystack)
        chk_str = ""
        rtn = -1
        for i in range(0, len(hs_list)):
            if len(hs_list) >= i + len(needle)-1:
                chk_str = "".join(hs_list[i:i + len(needle)])
                if chk_str == needle:
                    rtn = i
                    break

        # 一番早かった処理
        # rtn = haystack.find(needle)

        # index()メソッドを使った処理
        # hs_list = list(haystack)
        # rtn = hs_list.index(needle) if needle in hs_list else -1
        return rtn
