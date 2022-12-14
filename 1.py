# using for loop
num=int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num," is not a prime number.")
            break
        else:
            print(num," is a prime number.")
            break
else:
    print(num," is not a prime number.")
            
        
# using while loop
    
"""num=int(input("Enter a number: "))
i = 2
flag = 0
while i<num:
    if num%i == 0:
        flag = 1          #If Yes,update flag value
        print (num,"is NOT a prime number!");
        break
    i = i + 1              #Updating the value of i on every iteration by 1
#checking the value of flag
if flag == 0:
    print (num,"is a prime number!");      #If Yes, Then it is a prime number
    """
