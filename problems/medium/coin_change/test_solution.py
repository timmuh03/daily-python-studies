import pytest
from problems.medium.coin_change.solution import Solution



@pytest.mark.parametrize("coins, amount, expected", [
    ([1, 2, 5], 11, 3),

    ([2], 3, -1),

    ([1], 0, 0)
])

def test_coinChange(coins, amount, expected):
    result = Solution().coinChange(coins, amount)
    assert result == expected, f"Failed on coins:{coins}, amount:{amount}, expected:{expected}, result:{result}"