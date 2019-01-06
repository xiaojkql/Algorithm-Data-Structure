class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if peak > prices[i]:  # 当遇到下降就立马计算前面上升的利润
                max_profit += peak - valley  # valley移动之前计算前面的利润
                valley = prices[i]  # valley 向前移动
                peak = valley
                print(1)
            else:
                peak = prices[i]

            print(valley,peak)
        max_profit += peak - valley
        return max_profit

    def maxProfitSimple(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

if __name__ == '__main__':
    prices = [1,2,3,4,5]
    solution = Solution()
    print(solution.maxProfit(prices))