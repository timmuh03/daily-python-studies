import pytest
from .solution import Solution

@pytest.mark.parametrize("n, w, maxWeight, expected", [
    (2, 3, 15,
     4),
    (3, 5, 20,
     4),
    (1, 1, 50,
     1),
    (400, 400, 50,
     0),
    (400, 1, 1000,
     1000),
    (20, 1, 500,
     400)
])

def test_maxContainers(n: int, w: int, maxWeight: int, expected: int):
    result = Solution().maxContainers(n, w, maxWeight)
    assert result == expected, f"Failed for n: {n}, w: {w}, maxWeight: {maxWeight}, "
    "expected:{expected}, result:{result}"