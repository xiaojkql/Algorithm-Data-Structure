# program array rotation
print(__doc__)
import array
'''
input: array of size n
input: rotation number d
output: the rotated array
'''

# method 1 using a temp array O(n) + O(d)
def arrayRotation1(arr,n,d):
    tempArr = array.array('i')
    for i in range(d):
        tempArr.append(arr[i])
    for i in range(n-d):
        arr[i] = arr[i+d]
    for i in range(d):
        arr[n-d+i] = tempArr[i]


# method 2 Rotate one by one O(n*d) O(1)
def leftRotate(arr,n,d):
    for i in range(d):
        leftRotatebyOne(arr,n)

def leftRotatebyOne(arr,n): # O(n),O(1)
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

# method 3
# O(n) O(1)
# 用低维来理解 [1,2,3,4,5,6,7,8] (arr,12,4)
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def rotateJuggling(arr,n,d):
    for i in range(gcd(n,d)):
        j = i
        temp = arr[i]
        while True:
            k = j + d
            if k>=n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

# method 4 O(n) O(1)
def reverseArr(arr,start,end): # 包含end
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def rotateReverse(arr,n,d):
    reverseArr(arr,0,d-1) # 包含d-1
    reverseArr(arr,d,n-1)
    reverseArr(arr,0,n-1)

if __name__ == "__main__":
    arr = array.array('i',[1,2,3,4,5,6,7,8])
    print("using method 1 :")
    arrayRotation1(arr,len(arr),3)
    for i in range(len(arr)):
        print(arr[i],end=' ')
    print("\nusing method 2 :")
    arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12])
    leftRotate(arr,len(arr),8)
    for i in range(len(arr)):
        print(arr[i],end=' ')
    print("\nusing juggling")
    arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    rotateJuggling(arr, len(arr), 5)
    for i in range(len(arr)):
        print(arr[i], end=' ')

    print("\nusing Reverse")
    arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    rotateReverse(arr, len(arr), 5)
    for i in range(len(arr)):
        print(arr[i], end=' ')