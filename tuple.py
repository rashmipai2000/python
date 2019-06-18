def inputval():
    x="a=b,c=d,e=f,g=h"
    return x
def compute(x):
    m=x.split(",")
    for i in range(len(m)):#to use 1 for loop insted of 2 for loops
        m[i]=m[i].split("=")
        m[i]=tuple(m[i])
    return m   
def output(m):#pass parameters to output function
    print(m)
def main():
    x=inputval()#assign the call of a function to a variable
    m=compute(x)
    c=output(m)
main()  #no need to assign and no parameter in main function  



    
