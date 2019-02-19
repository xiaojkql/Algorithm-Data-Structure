# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # 思想逆转前一半，与后一半进行比较
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        revList = None
        fast = head
        slow = head
        while fast and fast.next:  # 提取一半的方法
            fast = fast.next.next
            # 三个同时赋值,不需要中间变量
            revList, revList.next, slow = slow, revList, slow.next
            """
            temp1 = slow.next
            slow.next = revList
            revList = slow
            slow = temp1
            和交换(a,b)是一样的
            """
        if fast:  # 当元素个数是奇数时向后移动一位
            slow = slow.next
        while revList and revList.val == slow.val:
            revList = revList.next
            slow = slow.next

        return not revList
