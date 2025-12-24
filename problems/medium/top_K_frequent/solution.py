"""
Docstring for problems.medium.top_K_frequent.solution
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counted_nums = Counter(nums)
        sorted_nums = sorted(counted_nums.items(), key=lambda item: item[1], reverse=True)
        return [num for num, _ in sorted_nums[:k]]