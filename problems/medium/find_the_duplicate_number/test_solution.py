import pytest
from problems.medium.find_the_duplicate_number.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([1,3,4,2,2], 2),
    ([3,1,3,4,2], 3),
    ([3,3,3,3,3], 3),
])


def test_findDuplicate(nums, expected):
    result = Solution().findDuplicate(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"