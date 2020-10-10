""" Module to test the QR decomposition using Householder transformations """

from ...src.householder.householder import qr, qr_errors
from .test_householder import gaussian_matrix
import numpy as np

np.random.seed(0)
np.set_printoptions(precision=10, linewidth=1000, suppress=True, threshold=1000)
TOL = 1e-13
N = 13
M = 17


def _test_qr(m, n):
    """
    Test that the QR decomposition works for m*n matrices, including both
    full-rank and low-rank matrics
    """
    A = gaussian_matrix(m, n)
    Q, R = qr(A)
    for e in qr_errors(A, Q, R):
        assert e < TOL

    for rank in range(4):
        A = gaussian_matrix(m, n, rank)
        Q, R = qr(A)
        for e in qr_errors(A, Q, R):
            assert e < TOL


def test_qr_square():
    """
    Test that the QR decomposition works for square matrices, including both
    full-rank and low-rank matrics
    """
    _test_qr(M, M)


def test_qr_skinny():
    """
    Test that the QR decomposition works for skinny matrices (more rows than
    columns), including both full-rank and low-rank matrics
    """
    _test_qr(M, N)


def test_qr_fat():
    """
    Test that the QR decomposition works for fat matrices (more columns than
    rows), including both full-rank and low-rank matrics
    """
    _test_qr(N, M)


def test_small_example():
    """ Test small 3x3 example from the Wikipedia page on QR decomposition """
    A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
    Q, R = qr(A)
    print("A=", A, "Q=", Q, "R=", R, sep="\n\n", file=open("Small QR example.txt", "w"))
    for e in qr_errors(A, Q, R):
        assert e < TOL


def test_integer_matrix():
    """ Test randomly generated integer matrix, and print output to file """
    A = np.random.choice(4, [10, 14]).astype(np.float)
    Q, R = qr(A, verbose=True)
    for e in qr_errors(A, Q, R):
        assert e < TOL
