# 557. Reverse Words in a String III
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        ans = []
        for item in s:
            ans.append(item[::-1])
        return " ".join(ans)

        # 要学会写简洁的代码
        # return " ".join([ans[::-1] for ans in s.split(" ")])
        # return " ".join(ans[::-1] for ans in s.split(" "))
        # return " ".join(s.split(" ")[::-1])[::-1] --> An amazing answer
