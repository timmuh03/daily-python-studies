import pytest
from .solution import Solution


@pytest.mark.parametrize("s, p, expected", [
    
    ("aaa", "a", [0,1,2]),
    ("cbaebabacd", "abc", [0, 6]),              
    ("abab", "ab", [0, 1, 2]),                  
    ("aaaaaaaaaa", "aaaa", [0, 1, 2, 3, 4, 5, 6]),
    ("baa", "aa", [1]),                         
    ("abcdefg", "hij", []),                     
    ("ab", "abc", []),                         
])

def test_findAnagrams(s, p, expected):
    result = Solution().findAnagrams(s, p)
    assert result == expected, f"Failed on s:{s}, p:{p}, expected:{expected}, result:{result}"