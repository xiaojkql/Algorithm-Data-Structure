# 67. Add Binary
# 两个二进制串相加，返回一个二进制串


class SolutionMine(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = []
        ia, ib, res = len(a)-1, len(b)-1, 0
        while ia >= 0 or ib >= 0:
            if ia >= 0:
                na = a[ia]
                ia -= 1
            else:
                na = 0
            if ib >= 0:
                nb = b[ib]
                ib -= 1
            else:
                nb = 0
            if int(na) + int(nb) + res > 2:
                ans.append(str(1))
                res = 1
            elif int(na) + int(nb) + res > 1:
                ans.append(str(0))
                res = 1
            else:
                ans.append(str(max(int(na), int(nb), res)))
                res = 0
        if res:
            ans.append(str(res))
        return "".join(ans[::-1])


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ""
        ia, ib, res = len(a)-1, len(b)-1, 0
        a, b = list(a), list(b)
        while ia >= 0 or ib >= 0 or res == 1:
            res += (int(a[ia])) if ia >= 0 else 0
            res += (int(b[ib])) if ib >= 0 else 0
            ans = str(res % 2)+ans
            res //= 2
            ia -= 1
            ib -= 1
        return ans


class SolutionSimple(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = int(a, 2) + int(b, 2)
        return bin(result)[2:]
