import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, divisors, expected", [
    ([3, 6, 9], [2, 3, 5],
     3),
    
    ([6, 12, 18], [3, 2, 5],
     2),
    
    ([1], [5, 7, 5],
     5),
    
    ([69,3,92,14,67,90,31,40,54,63,99,88,28,100,5,72,89,60,90,71], [97,16,7,60,6,57,73,84,17,8,77,60,7,74,74,24,52,43,94,48,9,99],
     9)
])

def test_max_div_score(nums, divisors, expected):
    sol = Solution()
    result = sol.maxDivScore(nums, divisors)
    assert result == expected, f"Failed on nums:{nums}, divisors:{divisors}, expected:{expected}, result:{result}"