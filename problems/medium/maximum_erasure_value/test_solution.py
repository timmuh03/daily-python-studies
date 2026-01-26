import pytest
from problems.medium.maximum_erasure_value.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([4,2,4,5,6], 17),
    ([5,2,1,2,5,2,1,2,5], 8)
])


def test_maximumUniqueSubarray(nums, expected):
    result = Solution().maximumUniqueSubarray(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"