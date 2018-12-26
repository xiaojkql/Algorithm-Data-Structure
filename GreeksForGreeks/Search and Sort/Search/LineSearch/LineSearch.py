# Line search algorithm

def lineSearch(arr,elem):
    '''

    :param arr: 被查找矩阵
    :param elem: 查找元素
    :return: index 或者 -1
    '''
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return -1

if __name__ == '__main__':
    arr = [12,4,5,0,7,8,9]
    print(lineSearch(arr,8))
    print(lineSearch(arr,100))