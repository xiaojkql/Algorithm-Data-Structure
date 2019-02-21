# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res, ans = 0, ListNode(1)
        nex = ans
        while l1 or l2 or res != 0:
            val1, val2 = 0, 0
            if l1:
                val1, l1 = l1.val, l1.next
            if l2:
                val2, l2 = l2.val, l2.next
            sum1 = val1+val2+res
            curr, res = sum1 % 10, sum1//10
            nex.next = ListNode(curr)
            nex = nex.next
        return ans.next
