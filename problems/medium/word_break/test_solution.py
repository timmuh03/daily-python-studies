import pytest
from problems.medium.word_break.solution import Solution



@pytest.mark.parametrize("s, wordDict, expected", [
    ("leetcode", ["leet", "code"], True),

    ("applepenapple", ["apple", "pen"], True),

    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),

    ("catsanddogs", ["cat", "cats", "and", "dog", "dogs"], True),

    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
     ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], False)
])

def test_wordBreak(s, wordDict, expected):
    result = Solution().wordBreak(s, wordDict)
    assert result == expected, f"Failed on s:{s}, wordDict:{wordDict}, expected:{expected}, result:{result}"