import pytest
from .solution import Solution


@pytest.mark.parametrize("s1, s2, expected", [
    ("ab", "eidbaooo", True),
    
    ("ab", "eidboaoo", False)
])


def test_checkInclusion(s1, s2, expected):
    result = Solution().checkInclusion(s1, s2)
    assert result == expected, f"Failed on s1:{s1}, s2:{s2}, expected:{expected}, result:{result}"