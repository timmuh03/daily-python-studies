import pytest
from problems.medium.car_fleet.solution import Solution



@pytest.mark.parametrize("target, position, speed, expected", [
    (12, [10,8,0,5,3], [2,4,1,1,3], 3),

    (10, [3], [3], 1),

    (100, [0,2,4], [4,2,1], 1),

    (10, [6,8], [3,2], 2)
])

def test_carFleet(target, position, speed, expected):
    result = Solution().carFleet(target, position, speed)
    assert result == expected, f"Failed on target:{target}, position:{position}, speed:{speed}, expected:{expected}, result:{result}"