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
    T = (dx/2) * np.sum(y_right + y_left)
    return T

print(trapz(np.sin,0,np.pi/2,1000))
''' output for thr above function
0.9999997943832332'''