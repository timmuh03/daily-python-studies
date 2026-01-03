import pytest
from koko_eating_bananas.solution import Solution



@pytest.mark.parametrize("piles, h, expected", [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30)
])



def test_minEatingSpeed(piles, h, expected):
    result = Solution().minEatingSpeed(piles, h)
    assert result == expected, f"Failed on piles:{piles}, h:{h}, expected:{expected}, result:{result}"