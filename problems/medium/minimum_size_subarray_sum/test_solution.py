import pytest
from minimum_size_subarray_sum.solution import Solution



@pytest.mark.parametrize("target, nums, expected", [
    (7, [2,3,1,2,4,3], 2,),
    (4, [1,4,4], 1),
    (11, [1,1,1,1,1,1,1,1], 0)
     
])



def test_minSubArrayLen(target, nums, expected):
    result = Solution().minSubArrayLen(target, nums)
    assert result == expected, f"Failed on target{target}, nums:{nums}, expected:{expected}, result:{result}"