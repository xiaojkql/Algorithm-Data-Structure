# array in python
import array
arr = array.array('i',[1,2,3])
print('The array is below: ')
print("The original array is: ",end=' ')
for i in range(len(arr)):
    print(arr[i],end=' ')

# use append method
arr.append(4)
print("\nThe array appended is: ",end=' ')
for i in range(len(arr)):
    print(arr[i],end=" ")

# use insert method
arr.insert(2,5)
print("\nThe array used insert is: ",end=' ')
for i in range(len(arr)):
    print(arr[i],end=" ")

# use pop method -->pop(index) reeturn arr[index]
print("\nUsing pop() method: ",arr.pop(),end=' ')
print("\nUsing pop(index) method: ",arr.pop(0),end=' ')

# use remove method --> remove(value) return none
# if the value doesn't exist, producing error
arr.remove(2)
print("\nAfter using pop and remove method: ",end=' ')
for i in range(len(arr)):
    print(arr[i],end=' ')

# use index() method
print('\nusing index method: ',arr.index(5))

# use reverse method
print("using reverse method: ",end=' ')
arr.reverse()
for i in range(len(arr)):
    print(arr[i],end=' ')

