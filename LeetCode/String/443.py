# 443. String Compression
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # two pointers
        slow, fast, prev, count = 0, 0, chars[0], 0
        while fast < len(chars):
            if chars[fast] == prev:
                count += 1
                fast += 1
            else:
                if count == 1:
                    chars[slow] = prev
                    slow += 1
                else:
                    chars[slow] = prev
                    slow += 1
                    st = []
                    while count // 10:
                        st.append(str(count % 10))
                        count //= 10
                    st.append(str(count))
                    while st:
                        chars[slow] = st.pop()
                        slow += 1
                    count = 1
                prev = chars[fast]
                fast += 1
        print(chars)
        if count > 1:
            chars[slow] = prev
            slow += 1
            st = []
            while count // 10:
                st.append(str(count % 10))
                count //= 10
            st.append(str(count))
            while st:
                chars[slow] = st.pop()
                slow += 1
        else:
            chars[slow] = prev
            slow += 1
        chars[:] = chars[:slow]


class SolutionSim(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # two pointers
        # 用了两个while循环来寻找
        slow, fast, prev, count = 0, 0, chars[0], 0
        while fast < len(chars):
            if chars[fast] == prev:
                count, fast = count+1, fast+1
            else:
                if count == 1:
                    chars[slow], slow = prev, slow+1
                else:
                    chars[slow], slow = prev, slow+1
                    if count > 1:
                        for s in str(count):
                            chars[slow], slow = s, slow+1
                    count = 1
                prev, fast = chars[fast], fast+1
        print(chars)
        if count > 1:
            chars[slow], slow = prev, slow+1
            for s in str(count):
                chars[slow], slow = s, slow+1
        else:
            chars[slow], slow = prev, slow+1
        chars[:] = chars[:slow]


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # two pointers
        slow, fast = 0, 0
        while fast < len(chars):
            ch, count = chars[fast], 0
            while fast < len(chars) and ch == chars[fast]:  # 再加了一个for循环
                fast, count = fast+1, count+1
            chars[slow], slow = ch, slow+1
            if count > 1:
                for s in str(count):
                    chars[slow], slow = s, slow+1
        return slow
