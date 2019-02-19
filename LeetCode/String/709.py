# 709. To Lower Case
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
        # return "".join([chr(ord(c)+32) if "A"<=c<="Z" else c for c in str])
        # return "".join([chr(ord(c)+32)
        # if 65<=ord(c)<=90 else c for c in str])
