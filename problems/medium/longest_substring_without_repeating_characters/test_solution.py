import pytest
from problems.medium.longest_substring_without_repeating_characters.solution import Solution



@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),

    ("bbbbb", 1),

    ("pwwkew", 3),

    ("abba", 2)
])

def test_lengthOfLongestSubstring(s, expected):
    result = Solution().lengthOfLongestSubstring(s)
    assert result == expected, f"Failed on s:{s}, expected:{expected}, result:{result}"