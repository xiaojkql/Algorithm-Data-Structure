
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        '''
        triangle = []
        for i in range(numRows):
            rows = [None for _ in range(i+1)]
            rows[0],rows[-1] = 1,1
            for j in range(1,i):
                rows[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(rows)

        return triangle
        '''

        # using map
        triangle = [[1]]  # 有一个初始化
        for i in range(1, numRows):
            map_ = map(lambda x, y: x + y, [0] + triangle[-1], triangle[-1] + [0])
            triangle.append(list(map_))

        return [] if not numRows else triangle

        res = [[1]]
        for _ in range(1, numRows):
            map_ = map(add, [0] + res[-1], res[-1] + [0])
            res.append(list(map_))
        return res if numRows else []