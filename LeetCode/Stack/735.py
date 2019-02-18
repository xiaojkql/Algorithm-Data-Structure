# 735. Asteroid Collision


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        for item in asteroids:
            ans.append(item)
            while len(ans) > 1 and ans[-2] > 0 and ans[-1] < 0:  # 这种形式的写法
                if abs(ans[-2]) > abs(ans[-1]):
                    ans.pop()
                elif abs(ans[-2]) < abs(ans[-1]):
                    ans[-2] = ans[-1]
                    ans.pop()
                else:
                    ans.pop()
                    ans.pop()
        return ans
