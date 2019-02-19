# Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: 'ListNode') -> 'ListNode':
        ans = head
        mark = head
        while mark and mark.next:
            ans = ans.next
            mark = mark.next.next
        return ans
