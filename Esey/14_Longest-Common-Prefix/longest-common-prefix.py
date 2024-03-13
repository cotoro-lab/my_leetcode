class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base_str = strs[0]
        common_str = ""

        for n in range(len(strs)):
            common_str = ""
            for i in range(len(base_str)):
                if i <= len(strs[n]) - 1 and base_str[i] == strs[n][i]:
                    common_str += base_str[i]
                else:
                    break
            base_str = common_str

        return common_str
