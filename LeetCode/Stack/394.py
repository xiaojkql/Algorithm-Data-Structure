class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = [["", 0]]
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                st.append(["", int(num)])
                num = ""
            elif ch == "]":
                last = st.pop()
                st[-1][0] += last[0]*last[1]
            else:
                st[-1][0] += ch
        return st[-1][0]
