import pytest
from problems.medium.find_minimum_in_rotated_sorted_array.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([3, 4, 5, 1, 2], 1),

    ([4, 5, 6, 7, 0, 1, 2], 0),

    ([11, 13, 15, 17], 11),

    ([1], 1),

    ([2, 3, 4, 5, 1], 1),

    ([2, 1], 1)
])

def test_findMin(nums, expected):
    result = Solution().findMin(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"