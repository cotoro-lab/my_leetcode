class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check_list = ["(", "{", "[", ")", "}", "]"]
        check_obj = []
        end_obj = []

        for s_unit in s:
            if s_unit in check_list:
                check_obj.append(s_unit)

        if len(check_obj) % 2 != 0:
            return False

        for i in range(len(check_obj)):
            if check_obj[i] in check_list[0:3]:
                end_obj.append(check_list.index(check_obj[i]) + 3)
                if len(end_obj) > len(check_obj) / 2:
                    return False
            else:
                if len(end_obj) == 0 \
                or check_list.index(check_obj[i]) != end_obj.pop():
                    return False

        if len(end_obj) != 0:
            return False
        
        return True


