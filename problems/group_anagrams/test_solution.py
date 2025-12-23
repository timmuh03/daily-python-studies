import pytest
from .solution import Solution


@pytest.mark.parametrize("strs, expected", [
    (["eat", "tea", "tan", "ate", "nat" "bat"],
     [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    
    ([""],
     [[""]]),
    
    (["a"],
     [["a"]])
])

def test_group_anagrams(strs, expected):
    result = Solution().groupAnagrams(strs)
    assert result == expected, f"Failed on strs:{strs}, expected:{expected}, result:{result}"