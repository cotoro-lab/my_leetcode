# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = str.rstrip(s).split(" ")
        return len(s_list[-1])

        # 引数なしだと連続した空文字を一つの区切りとして扱われる為
        # これで良いみたい
        # s_list = strip(s).split()