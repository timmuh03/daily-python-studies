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
        
        # using counter to produce easily readable code
        perm = Counter(s1)
        window = Counter(s2[:len(s1)])
        for i, char in enumerate(s2[:-len(s1)]):
            if window == perm:
                return True
            window[char] -= 1
            if window[char] == 0:
                del window[char]
            window[s2[i + len(s1)]] += 1
            
            
        return window == perm
        
        # *********************************************************
        # this code does the same but with lower constant overhead
        # using a fixed-size array and mismatch tracking
        # *********************************************************
        #
        # if len(s1) > len(s2):
        #     return False
        
        # def update_diff(idx, delta):
        #     nonlocal diff_count
        #     before = char_bucket[idx]
        #     char_bucket[idx] += delta
        #     after = char_bucket[idx]
        #     if before == 0 and after != 0:
        #         diff_count += 1 
        #     elif before !=0 and after == 0:
        #         diff_count -= 1
        
        # char_bucket = [0] * 26
        # diff_count = 0
        # window = len(s1)

        # for i in range(len(s1)):
            
        #     update_diff(ord(s1[i]) - ord('a'), 1)
        #     update_diff(ord(s2[i]) - ord('a'), -1)
                
        # if diff_count == 0:
        #     return True
                
        # for i in range(0, len(s2) - window):
        #     outgoing = s2[i]
        #     incoming = s2[i+window]
            
        #     update_diff(ord(outgoing) - ord('a'), 1)
        #     update_diff(ord(incoming) - ord('a'), -1)
            
        #     if diff_count == 0:
        #         return True
            
        # return False
    
