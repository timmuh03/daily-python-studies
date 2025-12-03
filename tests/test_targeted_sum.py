import pytest
from targeted_sum.solution import Solution

@pytest.mark.parametrize("arr, target, expected", [                   

([2, 7, 11, 15], 9, [0, 1]),
([1, 2, 3, 4], 100, "Target not found"),
([-3, 4, 1, 2], -1, [0, 3]),
([0, 4, 3, 0], 0, [0, 3]),
([1, 5, 5, 3], 10, [1, 2]),
([7], 7, "Array length error"),
([], 10, "Array length error"),
([10**9, 3, -10**9], 3, "Target not found"),
([8, 1, 2, 9, 5, 4], 9, [0, 1]),
([3, 3, 3], 6, [0, 1]),
([-10, 20, 5, -5], 10, [0, 1]),
([1.5, 2.5, 3.0], 4.0, [0, 1])

])

def test_find_target(arr, target, expected):
    sol = Solution()
    result = sol.find_target(arr, target)
    assert result == expected, f"Failed for arr:{arr}, target:{target}"