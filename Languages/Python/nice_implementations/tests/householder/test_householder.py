""" Module to test the Householder class for Householder transformations """

from ...src.householder.householder import Householder
import numpy as np
from numpy.linalg import norm

np.random.seed(0)
TOL = 1e-15
N = 10
M = 12


def gaussian_vector(m):
    """ Generate an m-dimensional Gaussian vector """
    return np.random.normal(size=m)


def gaussian_matrix(m, n, r=None):
    """
    Generate an m*n matrix using Gaussian random numbers. If r is None, the
    matrix will almost surely be full rank; otherwise, if r is a non-negative
    integer, the matrix will have rank r.
    """
    if r is None:
        return np.random.normal(size=[m, n])
    else:
        A = np.zeros([m, n])
        for _ in range(r):
            A += np.outer(gaussian_vector(m), gaussian_vector(n))

        return A


def test_symmetric():
    """ Test that the Householder matrix is symmetric """
    x, y = gaussian_vector(N), gaussian_vector(N)
    h = Householder(x, y)
    P = h.get_matrix()
    assert np.allclose(P, P.T, 0, TOL)


def test_orthogonal():
    """ Test that the Householder matrix is orthogonal """
    x, y = gaussian_vector(N), gaussian_vector(N)
    h = Householder(x, y)
    P = h.get_matrix()
    assert np.allclose(P @ P.T, np.identity(N), 0, TOL)


def test_self_inverse():
    """ Test that the Householder transformation is self-inverse """
    x, y = gaussian_vector(N), gaussian_vector(N)
    h = Householder(x, y)
    assert np.allclose(x, h @ (h @ x), 0, TOL)
    P = h.get_matrix()
    assert np.allclose(P @ P, np.identity(N), 0, TOL)


def test_householder_multiplication():
    """
    Test that the efficient Householder transform implementation is equivalent
    to matrix multiplication
    """
    x, y = gaussian_vector(N), gaussian_vector(N)
    h = Householder(x, y)
    z = gaussian_matrix(N, M)
    assert np.allclose(h @ z, h.get_matrix() @ z, 0, TOL)


def test_householder_direction():
    """
    Test that the Householder transform points vectors in the correct direction
    """
    x, y = gaussian_vector(N), gaussian_vector(N)
    h = Householder(x, y)
    z = h @ x
    assert np.allclose(z / norm(z), y / norm(y), 0, TOL)


def test_zero_input():
    """
    Verify that if x is a zero-vector, then the Householder transform for any
    given y is the identity transformation
    """
    x, y = np.zeros(N), gaussian_vector(N)
    h = Householder(x, y)
    assert np.allclose(h.get_matrix(), np.identity(N), 0, TOL)


def test_zero_out_column():
    """
    Test using a Householder transform to zero out the sub-diagonal of the first
    column of a matrix
    """
    A = gaussian_matrix(M, N)
    y = np.zeros(M)
    y[0] = 1
    h = Householder(A[:, 0], y)
    B = h @ A
    assert np.allclose(B[1:, 0], 0, 0, TOL)
