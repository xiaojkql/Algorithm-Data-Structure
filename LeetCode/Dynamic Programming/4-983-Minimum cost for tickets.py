class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(365+1)
        for i in range(1,365+1):
            if i in days:
                # max用的很巧妙
                dp[i] = min(dp[i-1]+costs[0],dp[max(i-7,0)]+costs[1],dp[max(i-30,0)]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[days[-1]]
