# 539. Minimum Time Difference
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        for i, time in enumerate(timePoints):
            time = time.split(":")
            timePoints[i] = int(time[0])*60+int(time[-1])
        timePoints.sort()
        return min(min([a-b for a, b in zip(timePoints[1:], timePoints)]),
                   24*60-timePoints[-1]+timePoints[0])  # 这种简洁的写法
