import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([0, 0, 0, 0],
     0),
    ([1, 1, 1, 2],
    2),
    ([10000000, 1, 3, 3],
    10000000),
    ([-2, -2, 0, 1],
     -2),
    ([2, 2, 4, 4, 6],
     2),
    ([4, 4, 2, 2, 1],
     2),
    ([-2, -2, -4, -4, -6],
     -4)
])

def test_mostFrequentEven(nums, expected):
    result = Solution().mostFrequentEven(nums)
    assert result == expected, f"Failed for nums:{nums}, expected:{expected}, result:{result}"