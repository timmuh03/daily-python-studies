import pytest
from .solution import Solution


@pytest.mark.parametrize("s, p, expected", [
    ("cbaebabacd", "abc", [0,6]),
    ("abab", "ab", [0,1,2])
])

def test_findAnagrams(s, p, expected):
    result = Solution().findAnagrams(s, p)
    assert result == expected, f"Failed on s:{s}, p:{p}, expected:{expected}, result:{result}"