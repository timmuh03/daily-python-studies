import pytest
from problems.medium.house_robber.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], 4),

    ([2, 7, 9, 3, 1], 12),

    ([2, 1, 1, 2], 4)
])

def test_rob(nums, expected):
    result = Solution().rob(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"