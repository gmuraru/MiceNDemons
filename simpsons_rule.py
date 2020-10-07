import numpy as np
try:
    ul = int(input("upper limit of the function : "))
    ll = int(input("lower limit of the function : "))
    n=4
    h=(ul-ll)/n
    print(h)
    x=[]
    s=0
    fx=[]
    print("enter the choice","\n","1. sqrt ", "\n", "2. sin", "\n","3. cos")
    choice = int(input())

    if(choice == 1):
        for i in range(0,n+1):
            inp = np.sqrt(s)
            fx.append(inp)
            x.append(s)
            s=s+h

    elif(choice == 2):
        for i in range(0,n+1):
            inp = np.sin(s)
            fx.append(inp)
            x.append(s)
            s=s+h
        
    elif(choice == 3):
        for i in range(0,n+1):
            inp = np.cos(s)
            fx.append(inp)
            x.append(s)
            s=s+h
    else:
        print("Kindly enter valid choice")
    
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

