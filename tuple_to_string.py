def inputtup():
    n=[('a','b'),('c','d'),('e','f'),('g','h')]
    return(n)
def convertstring(n):
    i=0;
    for x in n:
        n[i]="=".join(x)
        i=i+1
    #m=tuple(n)
    p=";".join(n)
    return p
def output(p):
    print(p)
def main():
    n=inputtup()
    p=convertstring(n)
    output(p)
main()
    
    
    





























    
