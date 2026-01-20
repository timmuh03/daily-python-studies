"""
Docstring for problems.medium.number_of_substrings_containing_all_three_characters.solution

Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c 
are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return -1