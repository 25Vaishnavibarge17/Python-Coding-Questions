# Method 1 : Using sorting
lst=[]
n=int(input("Enter size of array: "))
for i in range(0,n):
    print("Enter element: ")
    ele=int(input())
    lst.append(ele)
lst.sort()
print("Second largest element: ",lst[-2])


# Method 2 :Without Using sort
arr=[]
n=int(input("Enter size of array: "))
for i in range(0,n):
    print("Enter element: ")
    ele=int(input())
    arr.append(ele)
def findLargest(arr):
    secondLargest = 0
    largest = min(arr)
 
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        else:
            secondLargest = max(secondLargest, arr[i])
 
    print("Second largest number is: ")
    return secondLargest
print(findLargest(arr));
    
