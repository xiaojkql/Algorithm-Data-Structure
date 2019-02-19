# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        """
        st = []
        while head:
            st.append(head)
            head = head.next
        if st:
            head = st.pop()
        while st:
            head.next = st.pop()
        return head
        """
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
        """

        def recurse(node, prev=None):
            if not node:
                return prev
            curr = node
            node = node.next
            curr.next = prev
            prev = curr
            return recurse(node, prev)
        return recurse(head)
