# 224. Basic Calculator
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        # "+" "-"只管控制符号
        # curr表示当前()里面的表达式的值
        i, lenS = 0, len(s)
        sign, curr = 1, 0
        while i < lenS:
            if s[i] == " ":
                i += 1
                continue
            if s[i] == "+":
                sign = 1
                i += 1
                continue
            if s[i] == "-":
                sign = -1
                i += 1
                continue
            if s[i] == "(":
                st.append(curr)
                st.append(sign)
                i += 1
                curr, sign = 0, 1  # reset
                continue
            if s[i] == ")":
                curr *= st.pop()
                curr += st.pop()
                i += 1
                continue
            if s[i].isdigit():
                digit = ""
                while i < lenS and s[i].isdigit():
                    digit += s[i]
                    i += 1
                curr += sign*int(digit)
        return curr
