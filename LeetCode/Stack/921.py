class Solution:
    def minAddToMakeValid(self, S: 'str') -> 'int':
        st = []
        count = 0
        for ch in S:
            if ch == "(":
                st.append(ch)
            else:
                if len(st) == 0:
                    count += 1
                else:
                    st.pop()
        count += len(st)
        return count
