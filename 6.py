array=[]
n =int(input("Enter size of array: "))
for i in range (0,n):
    print("Enter array element: ")
    ele=int(input())
    array.append(ele)
summ=int(input("Enter the sum for which you have to search the pairs from array:  "))
print("Piars whose sum is ",summ," are : ")
for i in range(0,n):
    for j in range(i,n):
        if(array[i]+array[j]==summ):
            print("[",array[i],",",array[j],"]")
