import pytest
from problems.medium.longest_palindromic_substring.solution import Solution



@pytest.mark.parametrize("s, expected", [
    ("babad", {"bab", "aba"}),

    ("cbbd", {"bb"}),

    ("abcdefg", {"a", "b", "c", "d", "e", "f", "g"}),

    ("abb", {"bb"})
])

def test_longestPalindrome(s, expected):
    result = Solution().longestPalindrome(s)
    assert result in expected, f"Failed on s:{s}, expected:{expected}, result:{result}"