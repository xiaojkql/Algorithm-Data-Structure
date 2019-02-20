class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 1
        ans = []
        for s in S.split(" "):  # 可以使用enumerate()函数获取第几个标号
            if s[0].lower() in ("a", "e", "i", "o", "u"):
                ans.append(s + "ma"+"a"*i)
                i += 1
            else:
                if len(s) > 1:
                    ans.append(s[1:]+s[0]+"ma"+"a"*i)
                else:
                    ans.append(s+"ma"+"a"*i)
                i += 1
        return " ".join(ans)
        # return " ".join(ans+"ma"+"a"*(i+1) if ans[0].lower()
        # in ("a","e","i","o","u") else ans[1:]+ans[0]+"ma"+"a"*(i+1)
        # if len(ans)>1 else ans+"ma"+"a"*(i+1) for i,ans in enumerate(S))
