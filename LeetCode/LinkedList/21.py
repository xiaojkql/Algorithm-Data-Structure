# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if not l1 or not l2:
        #    return l1 or l2

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            ans = l1
            l1 = l1.next
        else:
            ans = l2
            l2 = l2.next
        mark = ans
        while l1 and l2:
            if l1.val < l2.val:
                mark.next = l1
                l1 = l1.next
            else:
                mark.next = l2
                l2 = l2.next
            mark = mark.next

        # mark.next = l1 or l2
        if l1:
            mark.next = l1
        if l2:
            mark.next = l2
        return ans


class SolutionRecurse(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 递归基
        # 有无返回，返回什么
        # 每一个递归回路应该比上一步减少什么
        if not l1 or not l2:
            return l1 or l2  # 写递归函数时，首先应该写出递归基
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)  # 每一个递归分路都应该逐步减少
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)  # 每一个递归分路都应该逐步减少
            return l2
