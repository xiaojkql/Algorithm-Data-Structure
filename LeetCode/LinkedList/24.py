# 24. Swap Nodes in Pairs
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        fast = head.next
        slow = head
        dum = ListNode(1)
        dum.next = head
        ans = dum
        while fast:
            fast.next, dum.next, slow.next = dum.next, slow.next, fast.next
            if not slow.next or not slow.next.next:
                break
            dum = slow
            fast = slow.next.next
            slow = slow.next
        return ans.next
