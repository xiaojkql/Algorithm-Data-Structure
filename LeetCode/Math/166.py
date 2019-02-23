# 166. Fraction to Recurring Decimal
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        pos = (numerator < 0) is (denominator < 0)
        ans = "" if pos else "-"
        nume, deno = abs(numerator), abs(denominator)
        inte, rest = nume//deno, nume % deno
        if not rest:
            return str(numerator/denominator)  # 如果能整除就直接返回
        ans += str(inte)+"."
        # 不能整除的情况
        i = len(ans)
        table = {}
        while rest:
            if rest not in table.keys():
                table[rest] = i
            else:
                i = table[rest]
                ans = ans[:i] + "(" + ans[i:]+")"
                return ans
            rest *= 10
            inte = rest//deno
            ans += str(inte)
            rest = rest % deno
            i += 1
        return ans
