import pytest
from subarray_sums_divisible_by_k import solution



@pytest.mark.parametrize("nums, k, expected", [
    ([4, 5, 0, -2, -3, 1], 5, 7),
    ([5], 9, 0)
])



def test_subarraysDivByK(nums, k, expected):
    result = solution.Solution().subarraysDivByK(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expected:{expected}, result:{result}"