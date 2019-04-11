class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        rows,cols = len(A),len(A[0])
        dp = [[0]*(cols) for _ in range(rows)]
        for i in range(cols):
            dp[0][i] = A[0][i]
        for i in range(1,rows):
            for j in range(cols):
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i-1][j],dp[i-1][j+1])
                elif j == cols-1:
                    dp[i][j] = A[i][j] + min(dp[i-1][j-1],dp[i-1][j])
                else:
                    dp[i][j] = A[i][j] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        return min(dp[rows-1])


class Solution1:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        rows,cols = len(A),len(A[0])
        dp = A[0]
        for row in range(1,rows):
            # 使用列表解析与一些函数可以简化代码量
            dp = [A[row][c]+min(dp[c],dp[max(c-1,0)],dp[min(cols-1,c+1)]) for c,value in enumerate(dp)]
        return min(dp)
