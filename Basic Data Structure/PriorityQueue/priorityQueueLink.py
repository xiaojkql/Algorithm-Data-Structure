# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 16:22:45
'''

# 基于底层是链表实现的优先级队列
import sys
sys.path.append(r"D:\MyGithub\Algorithm\Basic Data Structure")
from Queue.node import Node
from Queue.queueLink import QueueLink


class PriorityQueue(QueueLink):
    def __init__(self, sourceCollections=None):
        QueueLink.__init__(self, sourceCollections)

    def add(self, newItem):
        newNode = Node(newItem, None)
        if self.isEmpty() or newItem >= self._rear._data:
            QueueLink.add(self, newItem)
        else:
            probe = self._front
            trailer = probe
            while ((newItem >= probe._data) and
                   (probe is not None)):
                trailer = probe
                probe = probe._next
            newNode = Node(newItem, probe)
            if trailer is probe:
                self._front = newNode
            else:
                trailer._next = newNode
        self._size += 1


# simpLe test
def main():
    pq = PriorityQueue([7, 2, 4, 5, 7, 3, 0, 1, 5, 100, 78, 200])
    print(pq)
    print(pq.pop())
    pq.add(80)
    print(pq)


if __name__ == "__main__":
    main()
