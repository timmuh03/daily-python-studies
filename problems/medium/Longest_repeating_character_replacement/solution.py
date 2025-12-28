"""
Docstring for problems.medium.Longest_repeating_character_replacement.solution
You are given a string s and an integer k. You can choose any character of the string and 
change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get 
after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tot_count = 0
        char_count = defaultdict(int)
        max_freq = 0
        left = 0
        best = 0
        for char in s:
            tot_count += 1
            char_count[char] += 1
            if char_count[char] > max_freq:
                max_freq = char_count[char]
            while tot_count > max_freq + k:
                tot_count -= 1
                char_count[s[left]] -= 1
                left += 1
            if tot_count > best:
                best = tot_count
                
        return best