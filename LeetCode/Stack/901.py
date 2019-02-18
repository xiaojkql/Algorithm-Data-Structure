class StockSpanner(object):

    def __init__(self):
        self._stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # 注意是连续小于当天的
        # 只有比当前小的才出栈
        # 只管前面，而不管后面
        res = 1
        while self._stack and self._stack[-1][0] <= price:
            res += self._stack.pop()[1]
        self._stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
