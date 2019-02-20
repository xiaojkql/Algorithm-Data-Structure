class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # 使用了filter函数
        # 使用了lambda 作用于一个可迭代对象的每一项上
        # 使用了sorted函数
        # 使用列表解析
        # string的find方法
        letter = [log for log in logs if log[-1].isalpha()]
        letter = filter(lambda l: l[l.find(" ")+1].isalpha(), logs)
        digit = filter(lambda l: l[l.find(" ")+1].isdigit(), logs)
        return sorted(letter, key=lambda l: (l[l.find(" "):],
                                             l[:l.find(" ")])) + digit
