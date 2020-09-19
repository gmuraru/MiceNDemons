import pytest

import numpy as np
from src import gauss_seidel_dummy
from src import gauss_seidel

GS_MAP = {
    "gs_dummy": gauss_seidel_dummy,
    "gs": gauss_seidel
}

@pytest.mark.parametrize("method_name", ("gs_dummy", "gs"))
def test_gauss_seidel_converge(method_name):
    method = GS_MAP[method_name]
    A = np.array([[16, 3],[7, -11]])
    b = np.array([11, 13])
    x = np.array([1, 1])

    result = method(A, b, x)
    assert np.allclose(result, np.array([0.8122, -0.6650]), rtol=1e-4)

@pytest.mark.parametrize("method_name", ("gs_dummy", "gs"))
def test_gauss_seidel_not_converge(method_name):
    method = GS_MAP[method_name]
    A = np.array([[2, 3],[5, 7]])
    b = np.array([11, 13])
    x = np.array([1, 1])

    result = method(A, b, x)
    assert not np.allclose(result, np.array([-38, 29]))
