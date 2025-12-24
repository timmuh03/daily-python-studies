import pytest
from .solution import Solution


@pytest.mark.parametrize("strs, expected", [
    (["eat", "tea", "tan", "ate", "nat", "bat"],
     [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    
    ([""],
     [[""]]),
    
    (["a"],
     [["a"]]),
    
    (["Tom Marvolo Riddle", "I am Lord Voldemort", "Harry Potter"],
     [["Harry Potter"], ["I am Lord Voldemort", "Tom Marvolo Riddle"]])
])

def test_group_anagrams(strs, expected):
    result = Solution().groupAnagrams(strs)
    normalize = lambda groups: set(tuple(sorted(group)) for group in groups)
    
    assert normalize(result) == normalize(expected), f"Failed on strs:{strs}, expected:{expected}, result:{result}"