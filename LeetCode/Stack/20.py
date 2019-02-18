class Solution:
    def isValid(self, s: 'str') -> 'bool':
        st = []
        match = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in ["(", "[", "{"]:
                st.append(ch)
            else:
                if not st:
                    return False
                if st.pop() != match[ch]:
                    return False
        return True if not st else False
