import pytest
from .solution import Solution

@pytest.mark.parametrize("n: int, w: int, maxWeight: int, expected: int", [
    (2, 3, 15,
     4),
    (3, 5, 20,
     4)
])

def test_maxContainers(n: int, w: int, maxWeight: int, expected: int):
    result = Solution().maxContainers(n, w, maxWeight)
    assert result == expected, f"Failed for n: {n}, w: {w}, maxWeight: {maxWeight}, "
    "expected:{expected}, result:{result}"