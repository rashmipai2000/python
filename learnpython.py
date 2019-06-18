a=int(input("enter the first number"))
b=int(input("enter the second number"))
def compare(a,b):
    if(a>b):
     return 0
    elif(a<b):
     return 1
    else:
     return 2

c=compare(a,b)
if(c==0):
    print(b)
elif(c==1):
    print(a)
else:
 print("the numbers are equal")

    
    

    
