# 831. Masking Personal Information
class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = ""
        if S[-1].isalpha():
            front, rear = S.split("@")
            front = front[0].lower()+"*"*5+front[-1].lower()
            f, r = [item.lower() for item in rear.split(".")]
            return front+"@"+f+"."+r
        else:
            ans, count, i = "", 0, len(S)-1
            for ch in S:
                if ch.isdigit():
                    ans += ch
            print(ans)
            if len(ans) > 10:
                ans = "+**-***-***-"+ans[-4:]
            else:
                ans = "***-***-"+ans[-4:]
            return ans
