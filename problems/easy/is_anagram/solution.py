"""
Docstring for problems.easy.is_anagram.solution
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return False if len(s) != len(t) else Counter(s.lower().replace(" ", "")) == \
            Counter(t.lower().replace(" ", ""))
    
    # I placed extra checks to normalize to fit my favorite anagram.