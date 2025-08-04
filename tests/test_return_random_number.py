from src.utils import return_random_number
import numpy as np


def test_return_random_number():
    seed = 42  # for reproducibility
    a = [1, 2.4, 300]
    b = [2, 3.5, 400]

    A = np.array(np.meshgrid(a, b)).T.reshape(-1, 2)

    np.random.seed(seed)
    results = np.zeros(A.shape[0])
    for idx, pair in enumerate(A):
        i, j = pair
        results[idx] = return_random_number(i, j)

    np.random.seed(seed)
    expected = np.zeros(A.shape[0])
    for idx, pair in enumerate(A):
        i, j = pair
        expected[idx] = np.random.uniform(i, j)
        assert isinstance(results[idx], float)
        assert min(i, j) <= results[idx] <= max(i, j)
        assert np.isclose(results[idx], expected[idx], atol=1e-5)

    np.random.seed(seed)
    expected = np.random.uniform(2.3, 5)
    np.random.seed(seed)

    result = return_random_number("2.3", "5")
    assert np.isclose(result, expected, atol=1e-5)
