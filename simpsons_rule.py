import numpy as np
try:
    ul = int(input("upper limit of the function : "))
    ll = int(input("lower limit of the function : "))
    n=4
    h=(ul-ll)/n
    x=[]
    s=0
    fx=[]
    for i in range(0,n+1):
        fx.append(np.sqrt(s))
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

    print("y = ", h*s/3)
    
except:
    print("Kindly enter valid input")
