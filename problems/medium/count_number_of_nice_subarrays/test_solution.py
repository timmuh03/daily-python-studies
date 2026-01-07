import pytest
from count_number_of_nice_subarrays.solution import Solution



@pytest.mark.parametrize("nums, k, expected", [
    ([1, 1, 2, 1, 1], 3, 2),
    ([2, 4, 6], 1, 0),
    ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2, 16)
])



def test_numberOfSubarrays(nums, k, expected):
    result = Solution().numberOfSubarrays(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expected:{expected}, result:{result}"