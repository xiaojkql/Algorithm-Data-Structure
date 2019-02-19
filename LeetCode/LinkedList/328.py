# 328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd1 = odd2 = odd3 = head
        ans = odd1
        even1 = even2 = even3 = head.next
        # 要么只剩最后一个奇数节点，要么都已经遍历完毕，就退出循环
        while odd3 and even3 and even3.next:
            odd3 = odd3.next.next  # 移动奇节点，始终可以移动，因为有even
            if odd3.next:
                even3 = even3.next.next  # 移动偶数节点，当上一步奇数节点不为空时就可以移动
                odd2.next = odd3
                odd2 = odd2.next
                even2.next = even3
                even2 = even2.next
            else:
                break
        if odd3:
            odd2.next = odd3
            odd2 = odd2.next
        odd2.next = even1
        even3.next = None
        return ans
