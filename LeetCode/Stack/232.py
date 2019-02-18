# 用栈实现队列，push O(1) pop O(1)
class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls1 = []
        self.ls2 = []  # 一个中间变量栈

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """
        while self.ls1:
            self.ls2.append(self.ls1.pop())

        self.ls1.append(x)
        while self.ls2:
            self.ls1.append(self.ls2.pop())

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.ls1.pop()

    def peek(self) -> 'int':
        """
        Get the front element.
        """
        return self.ls1[-1]

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        return not self.ls1


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls1 = []
        self.ls2 = []  # 一个中间变量栈

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """
        self.ls1.append(x)

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.ls2.pop()

    def peek(self) -> 'int':
        """
        Get the front element.
        """
        if not self.ls2:
            while self.ls1:
                self.ls2.append(self.ls1.pop())
        return self.ls2[-1]

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        return (not self.ls1) and (not self.ls2)
