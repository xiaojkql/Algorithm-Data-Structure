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


if __name__ == "__main__":
    test4()
