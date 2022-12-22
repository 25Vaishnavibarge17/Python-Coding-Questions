# Brute force method without recursion
num=int(input("Enter a number: "))
summ=0
while num!=0:
    digit=num%10
    summ+=digit
    num=num//10
print(summ)

# Recursion method
num1=int(input("Enter a number: "))
sum1=0
def findsum(num1,sum1):
    if num1==0:
        return sum1
    digit=num1%10
    sum1+=digit
    return findsum((num1//10),sum1)
print(findsum(num1,sum1))

#one line code
n = [int(d) for d in input("Enter the number : ")]
print("the sum of digits is : ", sum(n))
