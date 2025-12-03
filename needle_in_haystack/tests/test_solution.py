import pytest
import sys
import os
from typing import Literal
from typing import LiteralString

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.solution import Solution


# Test cases for needle_in_haystack

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
def test_strStr(haystack: str, needle: str, expected: int):
    sol = Solution()
    result = sol.strStr(haystack, needle)
    assert result == expected, "Failed for haystack='{haystack}' needle='{needle}'"