# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-15 22:41:27
'''

# list 数据结构用python语言实现


class Node:
    def __init__(self, data):  # 构造函数
        self.data = data  # 数据项用来存取数据
        self.next = None  # 指针项pointer，指向下一个节点，也就是存储下一个节点的类


class LinkedList:
    def __init__(self):
        self.head = None  # 创建一个LinkedList也就是创建一个首节点

    def traverse(self):  # 遍历整个list中的元素
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    # 插入元素
    # 插在最前端
    def push(self, newData):
        node = Node(newData)
        node.next = self.head
        self.head = node

    # 插在末端
    def append(self, newData):
        node = Node(newData)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = node

    # 插在中间的某个位置 单项列表，只能作为某个节点的后面插入
    def insertAsAfter(self, pos, newData):
        node = Node(newData)
        node.next = pos.next
        pos.next = node

    # 给定一个值，如果存在就删除，如果不存在就什么都不做
    def deleteNode(self, val):
        tempNode = self.head
        if (tempNode is None):
            return
        if tempNode.data == val:
            self.head = tempNode.next
            tempNode = None
            return

        while(tempNode is not None):
            # 第一个元素已经提前判断了,所以一定不会再第一个就满足了退出
            if tempNode.data == val:
                break
            else:
                prev = tempNode
                tempNode = tempNode.next

        if (tempNode is None):
            return

        prev.next = tempNode.next
        tempNode = None
        return


if __name__ == "__main__":
    llist = LinkedList()
    # 创建节点
    # ls.head -> first.next -> second.next -> third.next --> None
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)

    llist.push(50)
    llist.append(10)
    llist.insertAsAfter(llist.head.next.next, 500)
    llist.traverse()
    llist.deleteNode(10)
    llist.deleteNode(500)
    print()
    llist.traverse()
