import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, target, expected", [
     # Target exists
    ([1, 3, 5, 6], 5, 2),

    # Target smaller than all
    ([1, 3, 5, 6], 0, 0),

    # Target larger than all
    ([1, 3, 5, 6], 7, 4),

    # Target fits in the middle
    ([1, 3, 5, 6], 4, 2),

    # Single element cases
    ([10], 5, 0),
    ([10], 20, 1),

    # Insert near the end
    ([2, 4, 6, 8], 7, 3),

    # Insert near the start
    ([2, 4, 6, 8], 3, 1),

    # All negatives
    ([-10, -3, -1], -5, 1),

    # Mix negatives + positives
    ([-3, -1, 4, 8], 0, 2),

    # Negative list, insert at end
    ([-5, -2, 0, 3], 5, 4),

    # Larger range
    ([1, 5, 20, 90, 300, 1000], 100, 4),
])

def test_search_insert_position(nums: list[int], target: int, expected: int):
    sol = Solution()
    result = sol.searchInsert(nums, target)
    assert result == expected, f"Failed for nums:{nums} - target:{target} - expected:{expected} - result:{result}"