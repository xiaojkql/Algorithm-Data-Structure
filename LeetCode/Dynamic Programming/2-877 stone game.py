class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i] # 只有一个石头的情形
        for dis in range(1,n):
            for i in range(0,n-dis):
                dp[i][i+dis] = max(piles[i]-dp[i+1][i+dis],piles[i+dis]-dp[i][i+dis-1])
        return dp[0][n-1]>0
