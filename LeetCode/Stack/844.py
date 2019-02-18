class Solution:
    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':
        S1 = []
        S2 = []
        for ch in S:
            if ch == "#":
                if len(S1):
                    S1.pop()
            else:
                S1.append(ch)

        for ch in T:
            if ch == "#":
                if len(S2):
                    S2.pop()
            else:
                S2.append(ch)
        return S1 == S2
