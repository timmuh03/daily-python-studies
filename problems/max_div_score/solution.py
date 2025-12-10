"""
Docstring for solution
You are given two integer arrays: nums and divisors.

The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].

Return the integer divisors[i] with the maximum divisibility score. If multiple integers have the maximum score, return the smallest one.
"""

from collections import defaultdict

class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        scores = defaultdict(int) # don't want to do multiple divisors
        
        for div in set(divisors):
            for num in nums:
                if num % div == 0:
                    scores[div] += 1 # don't need to check if it's not in the dict because of defaultdict
        if not scores:  # if nothing was divisible
            return min(divisors)
        
        high_score = max(scores.values())
       
        # check for ties and return smallest divisor
        return min(div for div, score in scores.items() if score == high_score)