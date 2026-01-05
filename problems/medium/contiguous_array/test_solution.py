import pytest
from contiguous_array.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([0, 1], 2),
    ([0, 1, 0], 2),
    ([0, 1, 1, 1, 1, 1, 0, 0, 0], 6)
])



def test_findMaxLength(nums, expected):
    result = Solution().findMaxLength(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"