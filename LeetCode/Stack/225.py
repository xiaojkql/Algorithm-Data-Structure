"""用队列实现栈"""
import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()

    def push(self, x: 'int') -> 'None':
        """
        Push element x onto stack.
        """
        self._queue.append(x)
        for i in range(len(self._queue)-1):
            self._queue.append(self._queue.popleft())

    def pop(self) -> 'int':
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._queue.popleft()

    def top(self) -> 'int':
        """
        Get the top element.
        """
        return self._queue[0]

    def empty(self) -> 'bool':
        """
        Returns whether the stack is empty.
        """
        return len(self._queue) == 0
