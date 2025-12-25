"""
Docstring for problems.most_frequent_even.solution
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.
"""
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
            # get dict items only if they're divisible by 2
        evens = Counter(num for num in nums if num % 2 == 0)
        
        if not evens:
            return -1
            # -evens[x] puts the most occuring nums as least, ties broken by smallest x
        return min(evens, key=lambda x: (-evens[x], x))