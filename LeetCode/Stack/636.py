class Solution:
    def exclusiveTime(self, n: 'int', logs: 'List[str]') -> 'List[int]':
        ans = [0]*n
        st = []
        prevTime = 0
        for log in logs:
            iD, mark, time = log.split(":")
            iD, time = int(iD), int(time)
            if mark == "start":
                if st:
                    ans[st[-1]] += time - prevTime
                st.append(iD)
                prevTime = time
            else:
                ans[st.pop()] += time - prevTime + 1
                prevTime = time + 1
        return ans
