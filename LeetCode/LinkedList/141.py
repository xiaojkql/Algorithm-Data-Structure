# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first = head
        second = head
        while first and second and first.next and second.next and second.next.next:
            first = first.next
            second = second.next.next
            if first is second:
                return True

        return False
