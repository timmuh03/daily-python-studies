"""
Docstring for problems.most_frequent_even.solution
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.
"""

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        evens = {}
        for num in nums:
            if num % 2 == 0:
                evens[num] = evens.get(num, 0) + 1
                
        max_freq = max(evens.values())
        
        if not evens:
            return -1
        
        most_freq = []
        for num, freq in evens.items():
            if freq == max_freq:
                most_freq.append(num)
                
        return min(most_freq)