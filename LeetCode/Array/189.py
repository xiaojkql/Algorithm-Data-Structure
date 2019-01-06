class Solution:
    def rotateBruteForce(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 指最后k个向前移动
        for i in range(k):
            temp = nums[-1]
            for j in range((len(nums)-1),0,-1):
                nums[j] = nums[j-1]
            nums[0] = temp

    def rotaterReverse(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # reverse method
        n = len(nums)  # 个数
        k = k % n
        mid = n - k  # 剩余个数
        self.reverse(nums, 0, mid - 1)
        self.reverse(nums, mid, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, arr, lo, hi):  # include hi
        while (lo < hi):
            temp = arr[lo]
            arr[lo] = arr[hi]
            arr[hi] = temp
            lo += 1
            hi -= 1

    def rotateTempArr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # using a temp arr
        k = k % len(nums)
        n = len(nums)
        tempArr = nums[0:n - k]
        nums[0:k] = nums[n - k:n]
        nums[k:n] = tempArr[:]

    def rotate(self, nums, d):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # using gca 精确查找移动后的位置
        d = d % len(nums)
        n = self.gca(d, len(nums))
        # 需要n个轮回
        for i in range(n):
            temp = nums[-1 - i]
            j = -1 - i
            while True:
                k = j - d # 以步长跳
                if k < -len(nums): # 超出范围
                    k = k  + len(nums)
                if k == -i-1:  # 回到原始处
                    break
                nums[j] = nums[k]
                j = k
            nums[j] = temp

    def gca(self, a, b):
        if b == 0:
            return a
        else:
            return self.gca(b, a % b)



if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10,11,12]

    solution = Solution()
    solution.rotate(nums,13)
    print(nums)

    '''
    solution = Solution()
    print(solution.gca(10,3))
    '''