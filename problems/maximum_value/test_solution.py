import pytest
from .solution import Solution

@pytest.mark.parametrize("strs, expected", [
    
    (["1234", "9999a", "0", "-1"],
     1234)
    
])

def test_maximum_value(strs, expected):
    result = Solution().maximumValue(strs)
    assert result == expected, f"Failed for strs:{strs}, expected:{expected}, result:{result}"
    
    