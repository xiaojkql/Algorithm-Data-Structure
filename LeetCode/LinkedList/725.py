# 725. Split Linked List in Parts
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # 思想：找长度
        rlen = 0
        ln = root
        while ln:
            rlen += 1
            ln = ln.next
        ans = []

        if rlen <= k:
            while k:
                if root:
                    temp, root, temp.next = root, root.next, None
                    ans.append(temp)
                else:
                    ans.append(None)
                k -= 1
        else:
            t1, t2 = rlen//k, rlen % k
            while k:
                head = root
                if t2:
                    for i in range(t1):
                        root = root.next
                    t2 -= 1
                else:
                    for i in range(t1-1):
                        root = root.next
                root.next, root = None, root.next
                ans.append(head)
                k -= 1
        return ans
