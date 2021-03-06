# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        def nestInteger(ls):
            if isinstance(ls, int):
                return NestedInteger(ls)
            lyst = NestedInteger()
            for item in ls:
                lyst.add(nestInteger(item))
            return lyst

        return nestInteger(eval(s))


class Solution1(object):
    def deserialize(self, s):
        # '-1' is not digit
        if s and s[-1].isdigit():
            return int(s)

        nested_integer = None
        digits = ''
        stack = []
        for c in s:
            if c.isdigit() or c == '-':
                digits += c
            elif c == '[':
                if nested_integer:
                    stack.append(nested_integer)
                nested_integer = NestedInteger()

            elif c == ']':
                if digits:
                    nested_integer.add(NestedInteger(int(digits)))
                    digits = ''
                if stack:
                    # 遇到"["且栈不为空时就出栈，以及何时添加此时的nest到其嵌套的里面的去
                    previous_nested_integer = stack.pop()
                    previous_nested_integer.add(nested_integer)
                    nested_integer = previous_nested_integer

            elif c == ',':
                if digits:
                    nested_integer.add(NestedInteger(int(digits)))
                    digits = ''

        return nested_integer
