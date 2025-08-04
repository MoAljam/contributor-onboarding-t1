from src.utils import return_random_number
import numpy as np


def test_return_random_number():
    a = [1, 2.4, 300]
    b = [2, 3.5, 400]

    # make all combinations of a and b
    A = np.array(np.meshgrid(a, b)).T.reshape(-1, 2)
    np.random.seed(42)  # for reproducibility

    for pair in A:
        i, j = pair
        random_number = return_random_number(i, j)
        assert isinstance(random_number, float)
        assert i <= random_number <= j or j <= random_number <= i
        assert np.isclose(random_number, np.random.uniform(i, j), atol=1e-5)
        assert np.isclose(return_random_number("2.3", "5"), np.random.uniform(2.3, 5), atol=1e-5)
