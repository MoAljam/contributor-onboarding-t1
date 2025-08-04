from src.utils import return_random_number
import numpy as np


def test_return_random_number():
    a = [1, 2.4, 300]
    b = [2, 3.5, 400]

    A = np.array(np.meshgrid(a, b)).T.reshape(-1, 2)
    np.random.seed(42)

    for pair in A:
        i, j = pair
        expected = np.random.uniform(i, j)
        result = return_random_number(i, j)
        assert isinstance(result, float)
        assert min(i, j) <= result <= max(i, j)
        assert np.isclose(result, expected, atol=1e-5)

    # Move this OUTSIDE the loop to avoid interfering with generator state
    np.random.seed(42)  # reset seed again for this test
    expected = np.random.uniform(2.3, 5)
    result = return_random_number("2.3", "5")
    assert np.isclose(result, expected, atol=1e-5)
