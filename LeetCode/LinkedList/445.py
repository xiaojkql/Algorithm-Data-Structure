# 445 Add Two Numbers II

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = ListNode(1)
        temp = 0
        while s1 or s2 or temp:
            temp1 = (s1.pop() if s1 else 0) + \
                    (s2.pop() if s2 else 0) + temp
            curr, temp = temp1 % 10, temp1//10
            """
            newNode = ListNode(curr)
            newNode.next = ans.next
            ans.next = newNode
            """
            # 操作顺序：先取出等号右边的项
            # 然后逐项赋给左边，并操作左边等式的每一项
            ans.next, ans.next.next = ListNode(curr), ans.next
        return ans.next
