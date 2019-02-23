# 43. Multiply Strings
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        pos = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                currSum = (ord(num1[i])-ord('0')) * \
                    (ord(num2[j])-ord('0')) + pos[i+j+1]  # 加上原来有的
                pos[i+j], pos[i+j+1] = pos[i+j]+currSum//10, currSum % 10
        return "".join(map(str, pos)).lstrip("0") or '0'
