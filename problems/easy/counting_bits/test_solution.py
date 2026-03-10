import pytest
from problems.easy.counting_bits.solution import Solution



@pytest.mark.parametrize("n, expected", [
    (2, [0, 1, 1]),

    (5, [0, 1, 1, 2, 1, 2])
])

def test_countBits(n, expected):
    result = Solution().countBits(n)
    assert result == expected, f"Failed on n:{n}, expected:{expected}, result:{result}"