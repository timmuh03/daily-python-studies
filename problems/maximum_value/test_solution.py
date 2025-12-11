import pytest
from .solution import Solution

@pytest.mark.parametrize("strs, expected", [
    
    (["1234", "9999a", "0", "-1"],
     1234),
    
    (["0"],
     0),
    
    (["-200", "$", "-201"],
     1),
    
    (["-1", "-2", "-3"],
     -1)
    
])

def test_maximum_value(strs, expected):
    result = Solution().maximumValue(strs)
    assert result == expected, f"Failed for strs:{strs}, expected:{expected}, result:{result}"
    
    