"""
Docstring for problems.medium.find_all_anagrams_in_a_string.solution
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""



from typing import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_count = Counter(p)
        result = []
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i:len(p)+i]) == p_count:
                result.append(i)
        return result
