def calc_LCM(x,y):
    if(x>y):
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0 and greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
    
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print("LCM of given to number is : ",calc_LCM(a,b))
