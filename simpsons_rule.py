import numpy as np
def func(s):
    return np.sqrt(s)

def simpsons_13rule(ul,ll,n):
    x=[]
    s=0
    fx=[]
    h=(ul-ll)/n
    for i in range(0,n+1):
        fx.append(func(s))
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
    print("y : ",simpsons_13rule(ul,ll,n))
    
except:
    print("Kindly enter valid input")
