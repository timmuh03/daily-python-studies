import pytest
from problems.medium.kth_largest_element_in_an_array.solution import Solution



@pytest.mark.parametrize("nums, k, expected", [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4)
])


def test_findKthLargest(nums, k, expected):
    result = Solution().findKthLargest(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expeceted:{expected}, result:{result}"