# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        first = headA
        second = headB
        while first is not second:
            first = first.next if first else headB
            second = second.next if second else headA
        return first


class SolutionStupid(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 解题思想，解题思路，问题的解决方案是关键啊
        a = headA
        b = headB
        lenA = 0
        lenB = 0
        while a or b:
            if a:
                lenA += 1
                a = a.next
            if b:
                lenB += 1
                b = b.next
        print(lenA, lenB)
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return headA
