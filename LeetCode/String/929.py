# 929. Unique Email Addresses


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # 使用python string模块的方法
        # split  join
        # 使用集合set
        s = set()
        for email in emails:
            localName, domainName = email.split("@")
            localName = "".join(localName.split("+")[0].split("."))
            s.add((localName+"@"+domainName))
        return len(s)
