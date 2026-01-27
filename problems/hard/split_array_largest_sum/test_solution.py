import pytest
from problems.hard.split_array_largest_sum.solution import Solution



@pytest.mark.parametrize("nums, k, expected", [
    ([7, 2, 5, 10, 8], 2, 18),
    ([1,2,3,4,5], 2, 9)
])


def test_splitArray(nums, k, expected):
    result = Solution().splitArray(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expected:{expected}, result:{result}"