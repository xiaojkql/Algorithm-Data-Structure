# 149. Max Points on a Line
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import collections
from decimal import Decimal


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # 用bruteforce,直线来进行判断
        lenP, maxLen = len(points), 1
        for i in range(lenP):
            slopes = collections.defaultdict(int)
            duplicate = 1
            for j in range(i+1, lenP):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                else:
                    if points[i].x == points[j].x:
                        slope = "vertical"
                    else:
                        slope = Decimal(
                            (points[i].y - points[j].y))/Decimal((points[i].x - points[j].x))
                    slopes[slope] += 1
                    print(slope)
                maxLen = max(maxLen, duplicate)
                for slope in slopes:
                    if slopes[slope]+duplicate > maxLen:
                        maxLen = slopes[slope]+duplicate
        return maxLen if points else 0


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
# from decimal import Decimal


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def gcdRe(a, b):
            return a if b == 0 else gcdRe(b, a % b)

        """
        def gcdIter(a,b):
            min_a_b,gcd = min(a,b),a
            while min_a_b:
        """

        # 用bruteforce,直线来进行判断
        lenP, maxLen = len(points), 1
        for i in range(lenP):
            slopes = collections.defaultdict(int)
            duplicate = 1
            for j in range(i+1, lenP):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                    continue
                else:
                    dx, dy = points[i].x - \
                        points[j].x, points[i].y - points[j].y
                    d = gcdRe(dx, dy)
                    slopes[(dx/d, dy/d)] += 1
            maxLen = max(maxLen, duplicate)
            for slope in slopes:
                if slopes[slope]+duplicate > maxLen:
                    maxLen = slopes[slope]+duplicate
        return maxLen if points else 0


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
# from decimal import Decimal


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        lenP, maxLen = len(points), 0
        for i in range(lenP):
            duplicate = 1
            for j in range(i+1, lenP):
                # 前面两个点不能重复
                x1, y1, x2, y2 = points[i].x, points[i].y, points[j].x, points[j].y
                if points[i].x == points[j].x and points[i].y == points[j].y:  # 除去重复的点
                    duplicate += 1
                    continue
                cnt = 0
                for k in range(lenP):
                    x3, y3 = points[k].x, points[k].y
                    if x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1 == 0:
                        cnt += 1
                maxLen = max(maxLen, cnt)
            maxLen = max(maxLen, duplicate)
        return maxLen
