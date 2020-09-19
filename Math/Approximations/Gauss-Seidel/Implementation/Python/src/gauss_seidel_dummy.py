import numpy as np

def gauss_seidel(A, b, x_init=None, rtol=1e-5, atol=1e-8, iter=1000):
    _, n = A.shape
    
    if x_init is None:
        """ Initial guess (if none given) is zero """
        x_init = np.zeros(n)
    
    x = np.array(x_init, dtype=np.float)

    for _ in range(iter):
        x_new = np.zeros(n, dtype=np.float)
        for i in range(n):
            S_lower = S_upper = 0

            for j in range(i):
                S_lower += A[i, j] * x_new[j]
            for j in range(i + 1, n):
                S_upper += A[i, j] * x[j]

            x_new[i] = (b[i] - S_lower - S_upper) / A[i, i]

        if np.allclose(x, x_new, rtol, atol):
            x = x_new
            break

        x = x_new

    return x
                