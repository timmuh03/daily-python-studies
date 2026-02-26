import pytest
from problems.medium.longest_consecutive_sequence.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
    ([1,0,1,2], 3)
])

def test_longestConsecutive(nums, expected):
    result = Solution().longestConsecutive(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"