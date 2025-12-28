import pytest
from .solution import Solution



@pytest.mark.parametrize("s, k, expected", [
    ("ABAB", 2, 4),
    
    ("AABABBA", 1, 4),
    
    ("EIAOBOO", 1, 4),
    
    ("AAAA", 2, 4),
    
    ("BBBBBBXYZXYZXYZ", 2, 8),  
    
    ("ABCDEABCDEABCDE", 1, 2),
   
])

def test_characterReplacement(s, k, expected):
    result = Solution().characterReplacement(s, k)
    assert result == expected, f"Failed on s:{s}, k:{k}, expected:{expected}, result:{result}"