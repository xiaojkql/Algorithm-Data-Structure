# 917. Reverse Only Letters
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letter = filter(lambda l: l.isalpha(), S)
        index = [i for i, s in enumerate(S) if s.isalpha()]
        letter = letter[::-1]
        ls = list(S)
        for i, j in enumerate(index):
            ls[j] = letter[i]
        return "".join(ls)


class SolutionStack(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letter = list(filter(lambda l: l.isalpha(), S))

        ans = [S[i] if not S[i].isalpha() else letter.pop()
               for i in range(len(S))]
        return "".join(ans)
