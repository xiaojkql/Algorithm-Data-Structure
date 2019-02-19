def test1():
    print("".join(str([1, 2, 3, 4])))
    return "-".join(str(item) for item in [1, 2, 3])
    # join(sequence) 接收一个可迭代的序列，
    # 但是元素一定要是string，不会发生自动转换的
    # str(list) -> strList


if __name__ == "__main__":
    print(str([0, 1, 2, 3, 4, 5, 6, 10]))
