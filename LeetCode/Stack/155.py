class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []

    def push(self, x: 'int') -> 'None':
        if self._items:
            if self._items[-1][1] < x:
                currMin = self._items[-1][1]
            else:
                currMin = x
        else:
            currMin = x
        self._items.append((x, currMin))

    def pop(self) -> 'None':
        return self._items.pop()[0]

    def top(self) -> 'int':
        return self._items[-1][0]
