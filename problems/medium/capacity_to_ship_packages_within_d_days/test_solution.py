import pytest
from capacity_to_ship_packages_within_d_days.solution import Solution



@pytest.mark.parametrize("weights, days, expected", [
    ([1,2,3,4,5,6,7,8,9,10], 5, 15),
    ([3,2,2,4,1,4], 3, 6),
    ([1,2,3,1,1], 4, 3)
])



def test_shipWithinDays(weights, days, expected):
    result = Solution().shipWithinDays(weights, days)
    assert result == expected, f"Failed on weights:{weights}, days:{days}, expected:{expected}, result:{result}"