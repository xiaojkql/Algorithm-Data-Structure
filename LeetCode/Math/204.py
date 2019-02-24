import math


import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        isPrime = [1]*n
        isPrime[0], isPrime[1] = 0, 0
        for i in range(2, n):
            j = 2
            if isPrime[i] == 1:
                while j*i < n:
                    isPrime[j*i] = 0
                    j += 1
        return sum(isPrime)


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        isPrime = [1]*n
        isPrime[0], isPrime[1] = 0, 0
        for i in range(2, int(math.sqrt(n)+1)):
            if isPrime[i]:
                isPrime[i*i:n:i] = [0]*len(isPrime[i*i:n:i])  # 这种赋值方式运行更快
        return sum(isPrime)


if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimes(15))
