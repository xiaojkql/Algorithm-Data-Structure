# 809. Expressive Words
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        lenS, ans = len(S), 0

        for word in words:
            lenW = len(word)
            if lenW == 0 or lenW > lenS:
                continue
            iS, iW, stretch = 0, 0, False  # 设置一个标志表示当前word的状态
            while iS < lenS and iW < lenW:
                if S[iS] == word[iW]:
                    currS, currW = iS, iW
                    while currS < lenS and S[currS] == S[iS]:
                        currS += 1
                    while currW < lenW and word[currW] == word[iW]:
                        currW += 1
                    # stretch:
                    if 3 <= currS-iS:
                        stretch = True
                        iS, iW = currS, currW
                        continue
                    # no stretch
                    elif currW-iW == currS-iS:
                        stretch = True
                        iS, iW = currS, currW
                        continue
                    # no stretch
                    else:
                        stretch = False
                        break
                else:
                    stretch = False
                    break
            print(iS, iW)
            if iS != lenS or iW != lenW:
                stretch = False
            if stretch:
                ans += 1
        return ans
