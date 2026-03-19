import pytest
from problems.medium.product_of_array_except_self.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),

    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
])

def test_productExceptSelf(nums, expected):
    result = Solution().productExceptSelf(nums)
    assert result == expected, f"Failed on nums:{nums} expected:{expected}, result:{result}"