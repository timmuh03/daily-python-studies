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
        n = len(s)
        if n < 3: return 0 # must have at least 3 chars to have a, b, and c

        # Updates char counts by delta(+1 for expanding, -1 for shrinking) for the current window.
        def buckets_delta(c, delta):
            nonlocal buckets
            if c == 'a':
                buckets[0] += 1 * delta
            elif c == 'b':
                buckets[1] += 1 * delta
            elif c == 'c':
                buckets[2] += 1 * delta


        buckets = [0,0,0] # [a,b,c]
        left = 0
        result = 0

        for i, char in enumerate(s):
            buckets_delta(char, 1)

            while 0 not in buckets:
                # Window is valid. All substrings left -> s[-1] are also valid
                result += n - i
                buckets_delta(s[left], -1)
                left += 1

        return result