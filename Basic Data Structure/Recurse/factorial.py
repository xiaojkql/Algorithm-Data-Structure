def factorial(n):
    if n == 1:
        return 1  # 递归基，不再调用其函数本身的时刻
    return n*factorial(n-1)


def Fibonacci(n):
    if n == 0:
        return 0  # 递归基，退化的情况
    if n == 1:
        return 1   # 递归基，退化的情况
    return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == "__main__":
    print(factorial(3))
    print(Fibonacci(5))
