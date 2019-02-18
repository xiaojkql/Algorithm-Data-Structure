# daily temperature
class Solution:
    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        ans = [0]*(len(T))
        st = []
        for i, item in enumerate(T):
            while st and T[st[-1]] < item:
                tail = st.pop()
                ans[tail] = i-tail
            st.append(i)
        return ans
