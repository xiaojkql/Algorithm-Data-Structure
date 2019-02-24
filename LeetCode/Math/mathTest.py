import operator
import functools
import collections
import math


def test1():
    print(float("inf"))


def test2():
    print(not "")


def test3():
    div, tmp = 1, 10
    while tmp >= 10:
        div = div*10
        tmp = tmp//10
    print(div)


def test4():
    t1, t2 = 5, 6
    print(t2 >> 1)
    print(not -1)


# python字符相减，C++支持：'a'-'b'但python不支持此操作
def test5():
    # print('a'-'b')  --> 错误的操作
    print(ord('a')-ord('b'))  # ord函数
    print(chr(78))  # 相应的chr函数


# test for (0)**-n
def test6():
    print(0**-4)  # --> 0没有负数指数幂


# test for unpack
def test7():
    x, n = 10, -1
    (x, n) = (x, n) if n >= 0 else (1/x, -n)  # 要加上括号表明清楚


# test for & 表示
# test for math module
def test8():
    print(math.pi)  # 3.1415926535....
    print(math.degrees(math.pi/4))  # 弧度到角度的变换函数
    print(math.e)  # 2.718281828459045
    print(math.exp(14))  # e**14
    print(math.fabs(-45))  # abs(x)
    print(math.factorial(45))  # x!
    print(math.floor(45.6))  # 45
    print(math.ceil(45.6))  # 46
    print(math.fmod(45, 4))  # 余数，float
    print(math.gcd(45, 6))  # 最大公约数
    print(math.hypot(3, 4))  # 返回以x,y为两直角边的斜边的长
    print(math.isnan())  # what's the function of this function


def test9():

    dic = collections.defaultdict(int)  # first arg must be collable
    for j in range(3):
        for i in range(4):
            dic[i] += 1
    print(dic)


def test10():
    pos = False is False
    print(pos)


def test11():
    print(26//26)


def test12Help(x, y):
    return x+y


# test for python functools reduce 模块
def test12():
    ls = [1, 2, 3, 4, 5, 6]
    print(functools.reduce(test12Help, ls))


def test13():
    s = set(1)
    print(s.add(1))


def test14():
    ls = [1, 2, 345]
    c = operator.itemgetter()


# test for sqrt
def test15():
    print(math.sqrt(12))


if __name__ == "__main__":
    test15()
