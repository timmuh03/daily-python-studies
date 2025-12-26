"""
Docstring for problems.medium.check_inclusion.solution
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = Counter(s1)
        window = Counter(s2[:len(s1)])
        for i, char in enumerate(s2[:-len(s1)]):
            print(f"perm:{perm}, window:{window}")
            if window == perm:
                return True
            window[char] -= 1
            if window[char] == 0:
                del window[char]
            window[s2[i + len(s1)]] += 1
            
            
        return window == perm