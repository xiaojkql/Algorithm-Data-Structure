class Solution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        # 思想： 遇到左压入，遇到右，计算score加到前一个值
        st = [0]
        for ch in S:
            if ch == "(":
                st.append(0)
            else:
                last = st.pop()
                st[-1] += 2*last or 1
        return st.pop()
