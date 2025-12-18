"""
Docstring for problems.num_of_strings.solution
Given an array of strings patterns and a string word, 
return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        if not patterns or not word:
            raise ValueError("Missing values")
        
        return sum(pat in word for pat in patterns)