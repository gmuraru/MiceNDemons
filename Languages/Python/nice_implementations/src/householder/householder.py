import numpy as np


class Householder:
    def __init__(self, x, y):
        """
        Initialise a householder transformation which transforms the vector x to
        point in the direction of a vector y, by reflecting x in a hyperplane
        through the origin, whose normal is denoted by v. The matrix of this
        linear transformation is denoted by P and is equal to I -
        2*v@v.T/(v.T@v) == I - beta*v@v.T, where beta = 2/(v.T@v). By
        definition, P@x == alpha*y for some scalar alpha.

        According to the derivation in section 5.1.2 of Matrix Computations by
        Golub and Van Loan (4th edition), expanding P = I - 2*v@v.T/(v.T@v) and
        P@x == alpha*y implies that v is parallel to x - alpha*y, and the
        magnitude of v is not unique, so we can set v = x - alpha*y. Expanding
        P@x - alpha*y == 0 implies that alpha**2 == (x.T@x)/(y.T@y)
        """
        alpha = np.linalg.norm(x) / np.linalg.norm(y)
        self.v = x - alpha * y
        denom = self.v.T @ self.v
        beta = 0 if denom == 0 else 2.0 / denom
        self.beta_times_v = beta * self.v

    def get_matrix(self):
        """
        Return the Householder matrix P == I - beta*(v @ v.T)
        """
        return np.identity(self.v.size) - np.outer(self.beta_times_v, self.v)

    def pre_mult(self, A):
        """
        Compute the matrix product P @ A:

        P @ A == (I - beta * v @ v.T) @ A == A - (beta * v) @ (v.T @ A)
        """
        return A - np.outer(self.beta_times_v, self.v.T @ A).reshape(A.shape)

    def __matmul__(self, A):
        return self.pre_mult(A)


def qr(A, verbose=False):
    """
    Compute the QR decomposition, A = Q @ R, where Q @ Q.T = I, and R is upper
    triangular, using Householder transformations.
    """
    m, n = A.shape
    y = np.zeros(m)
    y[0] = 1
    R = A.copy()
    k = min(m, n)
    h_list = [None] * k
    if verbose:
        f = open("qr.txt", "w")

    # Iterate through columns of A
    for i in range(k):
        # Apply Householder transform to sub-matrix to remove sub-diagonal
        if verbose:
            print("i={}\n".format(i), R, file=f, end="\n\n")
        h = Householder(R[i:, i], y[: m - i])
        h_list[i] = h
        R[i:, i:] = h @ R[i:, i:]

    # Create Q matrix from list of Householder transformations
    Q = np.identity(A.shape[0])
    for i in reversed(range(k)):
        Q[i:, i:] = h_list[i] @ Q[i:, i:]

    if verbose:
        print(
            "A=", A, "R=", R, "Q=", Q, "Errors=", qr_errors(A, Q, R), file=f, sep="\n\n"
        )

    return Q, R


def qr_errors(A, Q, R):
    recon_error = np.max(np.abs(A - Q @ R))
    ortho_error = np.max(np.abs(np.identity(A.shape[0]) - Q @ Q.T))
    triang_error = np.max(np.abs([e for i in range(R.shape[1]) for e in R[i + 1 :, i]]))
    return recon_error, ortho_error, triang_error
