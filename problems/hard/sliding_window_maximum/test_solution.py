import pytest
from problems.hard.sliding_window_maximum.solution import Solution



@pytest.mark.parametrize("nums, k, expected", [
    ([1,3,-1,-3,5,3,6,7], 3,
     [3,3,5,5,6,7]),

     ([1, -1, 3], 3,
      [3])
])

def test_maxSlidingWindow(nums, k, expected):
    result = Solution().maxSlidingWindow(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expected:{expected}, result:{result}"