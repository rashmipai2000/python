i=0
sum=0
n=int(input("enter the number of values"))
if(n==0):
    print("n cannot be zero")
else:
    for i in range(0,n,1):
        j=int(input("enter the number"))
        sum=sum+j
print("the sum is=",sum)        
        
