import pytest
from .solution import Solution


@pytest.mark.parametrize("n, m, expected", [
    (10, 3, 19),
    (5, 6, 15),
    (5, 1, -15)
])

def test_difference_of_sums(n, m, expected):
    result = Solution().differenceOfSums(n, m)
    assert result == expected, f"Failed on n:{n}, m:{m}, expected:{expected}, result:{result}"