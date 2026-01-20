import pytest
from problems.medium.number_of_substrings_containing_all_three_characters.solution import Solution



@pytest.mark.parametrize("s, expected", [
    ('abcabc', 10),
    ('aaacb', 3),
    ('abc', 1)
])


def test_numberOfSubstrings(s, expected):
    result = Solution().numberOfSubstrings(s)
    assert result == expected, f"Failed on s:{s}, expected:{expected}, result:{result}"