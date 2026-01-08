"""
Docstring for problems.medium.contiuous_subarray_sum.solution
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:
A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 
Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""


from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        current_mod = 0
        index_prime ={0: -1}

        for i, num in enumerate(nums):
            current_mod = (num + current_mod) % k
            if current_mod in index_prime:
                if i - index_prime[current_mod] >= 2:
                    return True
            else:
                index_prime[current_mod] = i

        return False