import pytest
from problems.medium.jump_game.solution import Solution



@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),

    ([3, 2, 1, 0, 4], False),

    ([0], True),

    ([2, 0, 0], True),

    ([1, 0, 1], False)
])

def test_canJump(nums, expected):
    result = Solution().canJump(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"