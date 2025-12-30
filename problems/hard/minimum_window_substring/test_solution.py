import pytest
from minimum_window_substring import solution


@pytest.mark.parametrize("s, t, expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("AAAXBC", "ABC", "AXBC"),
    ("AABBC", "ABC", "ABBC"),
    ("ABBBC", "ABC", "ABBBC")
])


def test_minWindow(s, t, expected):
    result = solution.Solution().minWindow(s, t)
    assert result == expected, f"Failed on s:{s}, t:{t}, expected:{expected}, result:{result}"