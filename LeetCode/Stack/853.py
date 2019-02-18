# car fleet


class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        times = [(target-p)/float(sp)
                 for (p, sp) in sorted(zip(position, speed))]
        ans = currTime = 0
        for time in times[::-1]:
            if time > currTime:
                ans += 1
                currTime = time
        return ans
