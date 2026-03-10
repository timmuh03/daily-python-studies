import pytest
from problems.medium.partition_equal_subset_sum.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([1, 5, 11, 5], True),

    ([1, 2, 3, 5], False),

    ([50, 2, 1, 3], False),

    ([1, 2, 5], False),

    ([2, 2, 3, 5], False),

    ([3, 3, 3, 4, 5], True),

    ([3, 3, 6, 8, 16, 16, 16, 18, 20], True),

    ([100, 1, 2, 3, 4, 90], True)
])

def test_canPartition(nums, expected):
    result = Solution().canPartition(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"