# 147. Insertion Sort List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dum = ListNode(1)
        dum.next = head
        endSorted = head
        head = head.next
        while head:
            # 新进元素比最后大于等于时
            if endSorted.val <= head.val:
                endSorted = endSorted.next
                head = head.next
            else:
                tmp = dum.next
                tmp1 = dum
                # 寻找插入位置
                while tmp.val < head.val:
                    tmp = tmp.next
                    tmp1 = tmp1.next
                tmp1.next, head.next, head = head, tmp, head.next
                endSorted.next = head
        return dum.next
