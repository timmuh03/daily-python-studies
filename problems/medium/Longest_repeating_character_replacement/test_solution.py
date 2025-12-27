import pytest
from .solution import Solution



@pytest.mark.parametrize("s, k, expected", [
    ("ABAB", 2, 4),
    
    ("AABABBA", 1, 4)
])

def test_characterReplacement(s, k, expected):
    result = Solution().characterReplacement(s, k)
    assert result == expected, f"Failed on s:{s}, k{k}, expected:{expected}, result:{result}"