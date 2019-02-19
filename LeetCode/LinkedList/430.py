# 430. Flatten a Multilevel Doubly Linked List
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        stack = []
        dum = Node(None, None, head, None)
        stack.append(head)
        head.prev = dum
        prev = dum
        while stack:

            # 出来一个提取一个元素
            # 设置新的链表连接方式
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
                curr.next = None  # 关键在这里设置了None 断了旧的链接
            if curr.child:
                stack.append(curr.child)  # 孩子后进栈，但是先出来
                curr.child = None

            prev = curr
        prev.next = None
        dum.next.prev = None
        return dum.next
