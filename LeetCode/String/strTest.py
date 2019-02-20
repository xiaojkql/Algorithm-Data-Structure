def test1():
    print("".join(str([1, 2, 3, 4])))
    return "-".join(str(item) for item in [1, 2, 3])
    # join(sequence) 接收一个可迭代的序列，
    # 但是元素一定要是string，不会发生自动转换的
    # str(list) -> strList


def test2():
    print(tuple([1, 2, 3, 4]))
    # tuple()元组接受的参数一定是一个可迭代对象
    # set() 也是接受一个可迭代对象
    # list() 接受一个可迭代对象
    a = set([1, 2, 3, 3, 4, 5, 6])
    print(a)


def test3(ls):  # 此ls指向了传递来的
    # ls = [7, 8, 9] 在改变之前不能赋给其他值，
    ls[1] = 12  # 能改变单个，能用切片改变
    ls[0:2] = [100, 200]
    ls = [7, 8, 9]  # 但是不能用这样的赋值方式


def test4():
    a = [1, 7, 2, 5, 6, 8, 1, 0, 1, 0]
    b = [item for item in a if item > 5]
    """
    当有多个if-else时if-else要放在for前面
    否则防在后面
    """
    c1 = " ".join(str(item) for item in a)
    c = " ".join(str(item) if item > 5 else str(item+10)
                 if item > 2 else str(item) for item in a)
    print(b)
    print(c)


def test5():
    s = "ab-cd"
    for ch in s:
        print(ch.isalpha())


def test6():
    ls = [1, 2, 3, 4, 5, 6]
    index = [0, 2, 4]
    ls[index] = [10, 20, 30]


# or 的使用
def test7():
    ls1 = [10, 20, 30, 4]
    ls2 = [0, 1, 2, 3]
    print(min(ls1 or ls2))  # --> 4
    ls1 = []
    ls2 = [0, 1, 2, 3]
    print(min(ls1 or ls2))  # --> 0


# string.find() 的使用
def test8():
    s = "LLLaaaaLL"
    print(s.find("aaa"))
    print(s.find(""))


# 测试filter，将满足条件的过滤出来
def test9():
    ls = [0, 1, 2, 3, 4, 5, 6]
    print(list(filter(lambda l: l < 2, ls)))


def test10():
    ls = []
    ls.append(1)
    print(ls)


def test11():
    a = "111"
    print(int(a, 2))
    print(bin(12))


# test for str.split()  当为空时，根据任何空格分裂
def test12():
    s = "xiao   jk  jksdf   fsdjf"
    print(s.split())


if __name__ == "__main__":
    # print(str([0, 1, 2, 3, 4, 5, 6, 10]))
    # ls = [4, 5, 6]
    # test3(ls)
    # print(ls)
    test12()
