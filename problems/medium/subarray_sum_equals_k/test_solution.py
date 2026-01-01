import pytest
from subarray_sum_equals_k import solution



@pytest.mark.parametrize("nums, k, expected", [
    ([1, 1, 1], 2, 2),
    ([1, 2, 3], 3, 2)
])



def test_subarrySum(nums, k, expected):
    result = solution.Solution().subarraySum(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expected:{expected}, result:{result}"