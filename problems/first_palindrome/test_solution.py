import pytest
from solution import Solution

@pytest.mark.parametrize("words, expected", [
    (["abc", "car", "ada", "racecar", "cool"],
     "ada"),
    
    (["notapalindrome", "racecar"], 
     "racecar"),
    
    ("none", "of", "these", "are", "palindromes",
     "")
    
])

def test_firstPalindrome(words, expected):
    result = Solution().firstPalindrome(words)
    assert result == expected, f"Failed on words:{words}, expected:{expected}, result:{result}"