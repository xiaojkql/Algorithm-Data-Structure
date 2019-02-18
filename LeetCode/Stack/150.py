# 150. Evaluate Reverse Polish Notation


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        for items in tokens:
            if items == "+":
                last = st.pop()
                st[-1] = st[-1] + last
            elif items == "*":
                last = st.pop()
                st[-1] = st[-1] * last
            elif items == "-":
                last = st.pop()
                st[-1] = st[-1] - last
            elif items == "/":
                last = st.pop()
                if last * st[-1] < 0 and st[-1] % last != 0:
                    st[-1] = st[-1]/last + 1
                else:
                    st[-1] = st[-1]/last
            else:
                st.append(int(items))
        return int(st[-1])
