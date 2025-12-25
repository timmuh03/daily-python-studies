import pytest
from .solution import Solution


@pytest.mark.parametrize("nums, expected", [
    ([0,1,1], [True, False, False]),
    
    ([1,1,1], [False, False, False]),
    
    ([0,0,0,], [True, True, True]),
    
    ([1, 0, 1], [False, False, True])
])


def test_prefixes_div_by_5(nums, expected):
    result = Solution().prefixesDivBy5(nums)
    assert result == expected, f"Failed on nums:{nums}, expected:{expected}, result:{result}"