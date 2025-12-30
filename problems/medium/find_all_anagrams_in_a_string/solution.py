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



from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # buckets = Counter(p)
        # result = []
        # for i in range(len(s) - len(p) + 1):
        #     if Counter(s[i:len(p)+i]) == buckets:
        #         result.append(i)
        # return result


        # O(n) sliding window using 26-len array + mismatch count
        
        buckets = [0] * 26
        result = []
        left = 0
        diff_count = 0

        def diff_count_delta(idx, delta):
            nonlocal diff_count
            before = buckets[ord(idx) - ord('a')]
            buckets[ord(idx) - ord('a')] += delta
            after = buckets[ord(idx) - ord('a')]

            if before == 0 and after != 0:
                diff_count += 1
            elif before != 0 and after == 0:
                diff_count -= 1

        for i in range(len(p)):
            diff_count_delta(p[i], 1)

        for i in range(len(s)):
            diff_count_delta(s[i], -1)
            if i - left >= len(p):
                diff_count_delta(s[left], 1)
                left += 1
            if diff_count == 0 and i - left + 1 == len(p):
                result.append(left)

        return result