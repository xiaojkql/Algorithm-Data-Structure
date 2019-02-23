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


if __name__ == "__main__":
    test7()
