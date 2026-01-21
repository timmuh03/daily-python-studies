import pytest
from problems.medium.fruit_into_baskets.solution import Solution



@pytest.mark.parametrize("fruits, expected", [
    ([1,2,1], 3),
    ([0,1,2,2], 3),
    ([1,2,3,2,2], 4)
])


def test_totalFruit(fruits, expected):
    result = Solution().totalFruit(fruits)
    assert result == expected, f"Failed on fruits:{fruits}, expected:{expected}, result:{result}"