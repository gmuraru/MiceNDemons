import numpy as np

def simpsons_13rule(ul,ll,n,func):
    x=[]
    s=0
    fx=[]
    h=(ul-ll)/n
    for i in range(0,n+1):
        func = np.cosh(s)
        fx.append(func)
        x.append(s)
        s=s+h
    
    s= 0
    for i in fx:
        if(fx.index(i) ==0 or fx.index(i) == len(fx)-1):
            s=s+i
            
    fx = fx[1:len(fx)-1]
    for i in fx:
        if(fx.index(i) % 2==0):
            s=s+ i*4
        else:
            s=s+i*2

    return (h*s/3)

try:
    ul = int(input("upper limit of the function : "))
    ll = int(input("lower limit of the function : "))
    n=4
    s=0
    func = np.cosh(s)
    print("y : ",simpsons_13rule(ul,ll,n,func))
    
except:
    print("Kindly enter valid input")

"""
**TEST CASES**
output for function simpsons_13rule(8,0,4,np.sin(s)) - 1.3301
output for function simpsons_13rule(8,0,4,np.cos(s)) - 1.14887
output for function simpsons_13rule(8,0,4,np.sinh(s)) - 1577.612
output for function simpsons_13rule(8,0,4,np.cosh(s)) - 1578.6713
"""
   

