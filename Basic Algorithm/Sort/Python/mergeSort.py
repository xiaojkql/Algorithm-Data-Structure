# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-15 19:15:27
'''

# 使用的策略是分而治之，将原始问题分解为两个问题而求解
# 不可以自我递归
# 复杂度为 nlogn T(n) = O(n) + T(n/2) + O(1)


class MergeSort():
    def version(self, nums, lo, hi):  # 不包含hi
        a = 1


def sortMerge(nums, lo, hi):
    if hi-lo < 2:
        return
    else:
        mi = (hi+lo) // 2
        sortMerge(nums, lo, mi)
        sortMerge(nums, mi, hi)
        merge(nums, lo, mi, hi)

# 实现时一个意思 传入有点问题
def merge(nums, lo, mi, hi):
    temp = [nums[i] for i in range(mi, hi)]  # 这是新的list
    i = mi - 1 
    j = hi-mi-1 # 还尚未插入的
    lenhi = hi-1 # 一定要注意不要改变传入的参数，数的复制时深复制
    while(i >= lo and j >= 0):        
        if temp[j] >= nums[i]:
            nums[lenhi] = temp[j]
            j -= 1
        else:
            nums[lenhi] = nums[i]
            i -= 1
        lenhi = lenhi - 1
    if j < 0:
        return
    else:
        nums[lo:lenhi+1] = temp[0:j+1]
        return


if __name__ == "__main__":
    sortC = MergeSort()
    nums = [5,4,6,75,23,5,6,1,2,3,100]
    sortMerge(nums,0,9)
    print(nums)
