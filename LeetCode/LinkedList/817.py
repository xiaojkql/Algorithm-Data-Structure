# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        setG = set(G)
        ans = 0
        while head:
            # 当遇到最后一个节点
            # 当当前节点值在集合中，但其下一个不在
            if head.val in setG and (not head.next or
                                     head.next.val not in setG):
                ans += 1
            head = head.next
        return ans
