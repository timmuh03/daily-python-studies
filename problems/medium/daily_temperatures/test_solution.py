import pytest
from daily_temperatures.solution import Solution



@pytest.mark.parametrize("temperatures, expected", [
    ([73, 74, 75, 71, 69, 72, 76, 73], 
     [1, 1, 4, 2, 1, 1, 0, 0]),

    ([30, 40, 50, 60],
     [1, 1, 1, 0]),

    ([30, 60, 90],
     [1, 1, 0])
])



def test_dailyTemperature(temperatures, expected):
    result = Solution().dailyTemperatures(temperatures)
    assert result == expected, f"Failed on temperatures:{temperatures}, expected:{expected}, result:{result}"