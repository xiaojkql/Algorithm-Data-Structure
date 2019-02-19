# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == m:
            return head
        dum = ListNode(0)
        dum.next = head
        revBeg = dum
        revEnd = dum
        n = n-m+1
        while m > 1:
            revBeg = revEnd = revBeg.next
            m -= 1
        revEnd = revEnd.next
        while n:
            revBeg.next, revEnd.next, revEnd = revEnd, revBeg.next, revEnd.next
            n -= 1
        return dum.next
