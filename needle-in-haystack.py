import pytest

'''
Docstring for needle-in-haystack
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass
        
        
        
# Test cases

@pytest.mark.parametrize("haystack, needle, expected", [
    # Basic
    ("hello", "ll", 2),
    ("hello", "lo", 3),
    ("aaaaa", "bba", -1),

    # Edge cases
    ("", "", 0),
    ("abc", "", 0),
    ("", "abc", -1),
    ("a", "", 0),

    # Needle longer
    ("short", "longer", -1),

    # Overlapping
    ("aaa", "aa", 0),
    ("aaaa", "aaa", 0),

    # Large inputs
    ("a"*10000, "a"*5000, 0),
    ("a"*9500 + "b"*500, "b"*500, 9500),

    # First occurrence
    ("mississippi", "iss", 1),
])
def test_find_needle(haystack, needle, expected):
    # Replace with your function name
    # assert find_needle(haystack, needle) == expected
    assert haystack.find(needle) if needle or haystack else 0 == expected