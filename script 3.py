a=10
b=8
c=9
def compare(a,b,c):
  if(a>b and a>c):
     return 0
  elif(b>a and b>c):
    return 1
  else:
    return 2
d=compare(a,b,c)
if(d==0):
    print("the greatest number=",a)
elif(d==1):
    print("the greatest number=",b)
else:
    print("the greatest number=",c)



