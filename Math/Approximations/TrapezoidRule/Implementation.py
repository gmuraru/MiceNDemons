import numpy as np


def trapz(f,a,b,N=50):
    '''The trapezoid rule approximates the integral int_a^b f(x) dx by the sum:
    (dx/2)/sum_{k=1}^N (f(x_k) + f(x_{k-1}))
    where x_k = a + k*dx and dx = (b - a)/N.
    '''
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    t = (dx/2) * np.sum(y_right + y_left)
    return t

print(trapz(lambda x : x**3 + x**2 + x + 1,0,1,10000))
''' output for thr function trapz(np.sin,0,np.pi/2,1000)
0.9999997943832332
output for thr function trapz(lambda x : 3*x**2,0,1,10000)
1.0000000050000002
output for thr function trapz(np.tan,0,np.pi/2,1000)
12826525394010.809
output for thr function trapz(lambda x : x**3 + x**2 + x + 1,0,1,10000)
2.0833333375000005
'''
