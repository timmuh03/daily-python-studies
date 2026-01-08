import pytest
from continuous_subarray_sum.solution import Solution



@pytest.mark.parametrize("nums, k, expected", [
    ([23, 2, 4, 6, 7], 6, True),
    ([23, 2, 6, 4, 7], 6, True),
    ([23, 2, 6, 4, 7], 13, False),
    ([23,2,4,6,6], 7, True),
    ([0], 1, False),
    ([5, 0, 0, 0], 3, True)
])


def test_checkSubarraySum(nums, k, expected):
    result = Solution().checkSubarraySum(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expected:{expected}, result:{result}"