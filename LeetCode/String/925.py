# 925. Long Pressed Name
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif typed[j] == typed[j-1]:  # 此时typed与name不相等则一定是多的
                j += 1
            else:
                return False
        return True if i == len(name) else False
