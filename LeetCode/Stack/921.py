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


class SolutionSimple:
    def minAddToMakeValid(self, S: 'str') -> 'int':
        right = left = 0
        for ch in S:
            if ch == "(":
                left += 1
            elif left == 0:
                right += 1
            else:
                left -= 1
        return right + left
