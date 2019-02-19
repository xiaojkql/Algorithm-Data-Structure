# 657. Robot Return to Origin
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        ud = lr = 0
        for ch in moves:
            if ch == "U":
                ud += 1
            elif ch == "D":
                ud -= 1
            elif ch == "L":
                lr += 1
            else:
                lr -= 1
        return True if ud == 0 and lr == 0 else False
        # return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
        # # 返回的是一个字典，关键字每一个元素，值：元素的个数
        # c = collections.Counter(moves)
        # return c["L"] == c["R"] and c["U"] == c["D"]
