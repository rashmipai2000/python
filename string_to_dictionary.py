def inputval():
    n="a=b,c=d,e=f,g=h"
    return(n)
def compute(n):
    m=n.split(",")
    for i in range(0,len(m)):
            m[i]=tuple(m[i].split("="))
    p=dict(m)
    return p
def output(p):
    print(p)
def main():
    x=inputval()
    n=compute(x)
    output(n)
main()

    
            
            
    
