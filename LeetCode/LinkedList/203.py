# 203. Remove Linked List Elements
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ans = head
        prev = head
        count = 0
        while head:
            if head.val == val:
                if count == 0:
                    head = head.next
                    prev = head
                    ans = head
                else:
                    prev.next = head.next
                    head = head.next
            else:
                prev = head
                head = head.next
                count += 1
        return ans


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 使用一个额外的节点
        dummy = ListNode(-1)  # 切记这里不能使用dummy = head
        dummy.next = head
        prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return dummy.next


class SolutionRecurse(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 递归的进入最后一个单元，
        # 当到达递归基时首先返回
        # 然后判断当前节点是否相等
        # 相等返回下一个，不相等返回当前

        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head
