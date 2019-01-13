class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        
        """
        # idea ： 将最大的排在最后面，然后依次排
        k = m + n - 1
        i = m - 1  # 第一个数组的最后一个元素
        j = n - 1  # 第二个数组的最后一个元素
        while i >=0 and j >=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        while j>=0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

    def merge2(self,nums1,m,nums2,n):
        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[0:n] = nums2[0:n]

if __name__ == "__main__":
    nums1 = [1,2,7,10,56,0,0,0,0,0,0,0]
    nums2 = [2,3,8,9,11,100]
    solution = Solution()
    solution.merge(nums1,5,nums2,6)
    print(nums1)