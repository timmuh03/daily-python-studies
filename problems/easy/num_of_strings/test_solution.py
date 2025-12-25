import pytest
from .solution import Solution

@pytest.mark.parametrize("patterns, word, expected", [
    (["a", "abc", "bc", "d"], "abc",
     3),
    (["a", "b", "c"], "aaaaabbbbb",
     2),
    (["a", "a", "a"], "ab",
     3),
])

def test_num_of_strings(patterns, word, expected):
    result = Solution().numOfStrings(patterns, word)
    assert result == expected, f"Failed on patterns:{patterns}, word:{word}, expected:{expected}, result:{result}"
    
def test_expected_error():
    with pytest.raises(ValueError):
        Solution().numOfStrings([""], "")