import pytest
from RansomNote import solution


@pytest.mark.parametrize("ransomNote, magazine, expected", [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("aa", "ab", False),
    ("a", "", False)
])

def test_canConstruct(ransomNote, magazine, expected):
    result = solution.Solution().canConstruct(ransomNote, magazine)
    assert result == expected, f"Failed on ransomNote:{ransomNote}, magazine:{magazine}, \
        expected:{expected}, result:{result}"