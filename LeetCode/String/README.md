#### 929 [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses)

题目：将邮件名称按照要求统一化。

解题思路：字符串的划分与串接。

#### 709 [To Lower Case](https://leetcode.com/problems/to-lower-case)

题目：将字符全部转化为小写。

解题思路：转换

#### 804 [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words)

题目：按照一定规则进行转换，然后返回独一无二的个数。

考点：字符串的串接，单个字符函数ord,chr,'a'-'z','A'-'Z','a'<'z'

解题思路：直接替换，然后用集合 **集合中的元素时独一无二的**

#### 657 [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin)

题目：

考点：字符中字符的计数

解题思路：count，collections.count()

#### 557 [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii)

题目：逆转字符串中的子字符串

```
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

解题思路：两次逆转最简单，单个单词的逆转，

python点：ls[::-1] 逆转，.join(sequence)的灵活使用

#### 344 [Reverse String](https://leetcode.com/problems/reverse-string)

题目：

#### 893 [Groups of Special-Equivalent Strings](https://leetcode.com/problems/groups-of-special-equivalent-strings)

题目：每个单词经过任意的奇数的index之间的字符或者偶数的index之间进行交换后，仍不相等的单词个数。

解题思路：想方设法形成一个集合，再来判断，提取奇数index上的与偶数index上的字符进行排序后的元组对。

python：tuple,join,slice

#### 937 [Reorder Log Files](https://leetcode.com/problems/reorder-log-files)

python: filter,lambda,s.find(),sorted(key)-->自己定义排序的关键字

