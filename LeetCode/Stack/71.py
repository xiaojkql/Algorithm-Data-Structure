# 71. Simplify Path


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [p for p in path.split('/') if p != '.' and p != ""]
        st = []
        for item in path:
            if item == "..":
                if st:
                    st.pop()
            else:
                st.append(item)
        return "/"+"/".join(st)
