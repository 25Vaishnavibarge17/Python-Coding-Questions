#Method 1: Iterative (without recursion)
num=int(input("Enter a number: "))
fact=1 
if num<0:
    print("Factorial of negative number do not exist")
elif num==0:
    print("Factorial of number 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial is : ",fact)    
    
#Method 2: Using Recursion   
num=int(input("Enter a number: "))
fact=1 
def factorial(num):
    if(num==1):
        return num
    else:
        return (num*factorial(num-1))
    
if num<0:
    print("Factorial of negative number do not exist")
elif num==0:
    print("Factorial of number 0 is 1")
else:
    print("Factorial of number",num," is ",factorial(num))
        
