size=int(input("Enter the number of elements you want in array: "))
arr=[]
revArr=[]
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
startIndex = 0;
lastIndex = size - 1;
while (lastIndex>=0):
    revArr.append(arr[lastIndex])
    startIndex+=1
    lastIndex-=1
print("Array in reverse order")
for i in range(0,size):     
    print(revArr[i],end=' ') 
