import pytest
from .solution import Solution


@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram",
     True),
    
    ("rat", "car",
     False),
    
    ("I am Lord Voldemort", "Tom Marvolo Riddle",
     True)
])


def test_is_anagram(s, t, expected):
    result = Solution().isAnagram(s, t)
    assert result == expected, f"Failed on s:{s}, t:{t}, expected:{expected}, result:{result}"