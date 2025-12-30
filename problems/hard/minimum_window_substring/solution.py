"""
Docstring for problems.hard.minimum_window_substring.solution

Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. If there is no such substring, 
return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""


from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        required = len(need)
        left_char = formed = 0
        best_len = float("inf")
        best_left = best_right = 0

        for i, char in enumerate(s):
            have[char] += 1
            if  char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                current_len = i - left_char + 1
                if current_len < best_len:
                    best_left = left_char
                    best_right = i + 1
                    best_len = current_len
                if s[left_char] in need and have[s[left_char]] == need[s[left_char]]:
                    formed -= 1
                have[s[left_char]] -= 1
                left_char += 1
                    

        return "" if best_len == float("inf") else s[best_left:best_right]