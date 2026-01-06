import pytest
from binary_subarrays_with_sum.solution import Solution



@pytest.mark.parametrize("nums, goal, expected", [
    ([1, 0, 1, 0, 1], 2, 4),
    ([0,0,0,0,0], 0, 15)
])



def test_numSubarrayWithSum(nums, goal, expected):
    result = Solution().numSubarraysWithSum(nums, goal)
    assert result == expected, f"Failed on nums:{nums}, goal:{goal}, expected:{expected}, result:{result}"