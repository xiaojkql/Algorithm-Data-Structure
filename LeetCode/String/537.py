# 537. Complex Number Multiplication
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a.split("+"), b.split("+")
        s = int(a[0])*int(b[0]) - int(a[1][:-1])*int(b[1][:-1])
        x = int(a[0])*int(b[1][:-1]) + int(a[1][:-1])*int(b[0])
        ans = str(s)+"+"+str(x)+"i"
        return ans
