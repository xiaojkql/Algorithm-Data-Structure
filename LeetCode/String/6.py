# 6. ZigZag Conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        z = [[] for _ in range(min(numRows, len(s)))]
        currRow, currDirec = 0, 1
        iS = 0
        while iS < len(s):
            arg = (1, numRows-1, 1) if currDirec > 0 else (numRows-2, 0, -1)
            if currDirec > 0:
                for i in range(numRows):
                    if iS >= len(s):
                        break
                    z[i].append(s[iS])
                    iS += 1
            else:
                for i in range(*arg):
                    if iS >= len(s):
                        break
                    z[i].append(s[iS])
                    iS += 1
            currDirec *= -1
        print(z)
        ans = "".join(["".join(item) for item in z])
        return ans


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        L = [""]*numRows
        index, step = 0, 1
        for ch in s:
            L[index] += ch
            if index == 0:
                step = 1
            if index == numRows-1:
                step = -1
            index += step
        return "".join(L)
