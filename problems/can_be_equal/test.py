import pytest
from .solution import Solution


@pytest.mark.parametrize("target, arr, expected", [
    # 1. Exact match
    ([1, 2, 3],
    [1, 2, 3],
    True),

    # 2. Reversed
    ([1, 2, 3],
    [3, 2, 1],
    True),

    # 3. Out-of-order but same values
    ([4, 1, 7, 3],
    [1, 3, 4, 7],
    True),

    # 4. Duplicate numbers (same counts)
    ([1, 2, 2, 3],
    [2, 1, 3, 2],
    True),

    # 5. Duplicate numbers (different counts)
    ([1, 1, 2],
    [1, 2, 2],
    False),

    # 6. Completely different numbers
    ([1, 2, 3],
    [4, 5, 6],
    False),

    # 7. One element — same
    ([5],
    [5],
    True),

    # 8. One element — different
    ([5],
    [6],
    False),
    
    # 9. Large numbers
    ([100000, -100000, 3],
    [3, 100000, -100000],
    True),

    # 10. Zero values
    ([0, 1, 0],
    [0, 0, 1],
    True),

    # 11. Same length but one mismatch
    ([1, 2, 3, 4],
    [1, 2, 3, 5],
    False),

    # 12. Long identical repeated pattern
    ([1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 2, 1],
    True)
])

def test_can_be_equal(target: list[int], arr: list[int], expected: bool):
    sol = Solution()
    result = sol.canBeEqual(target, arr)
    assert result == expected, f"Failed for target: {target}, arr: {arr}"