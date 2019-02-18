# 体现使用stack这种数据结构的思想


class Solution:
    def calPoints(self, ops: 'List[str]') -> 'int':
        score = []
        for ch in ops:
            if ch == "C":
                score.pop()
            elif ch == "+":
                score.append(score[-1]+score[-2])
            elif ch == "D":
                score.append(score[-1]*2)
            else:
                score.append(int(ch))
        return sum(score)


if __name__ == "__main__":
    ls = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    sol = Solution()
    print(sol.calPoints(ls))
