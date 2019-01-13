class Solution:
    def fib(self, N):
        """
        普通的迭代方法
        :type N: int
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a+b  # 此处交换时，b，与 a + b都是之前的数进行运算的，将运算结果赋值给两个数
        return a

    def fibmine(self, N):
        if N == 0 or N == 1:
            return N
        pre = 0
        nex = 1
        while N-2 >= 0:
            pre, nex = nex, nex+pre
            N -= 1
        return nex

    def fib_list(self, N):
        fb = [0, 1]
        if N == 0:
            return N
        for i in range(N-1):
            fb.append(fb[-1]+fb[-2])
        return fb[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(5))
