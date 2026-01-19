import pytest
from problems.medium.subarray_product_less_than_k.solution import Solution



@pytest.mark.parametrize("nums, k, expected", [
    ([10,5,2,6], 100, 8),

    ([1,2,3], 0, 0),

    ([10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19, 18)
])


def test_numSubarrayProductLessThanK(nums, k, expected):
    result = Solution().numSubarrayProductLessThanK(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expected:{expected}, result:{result}"