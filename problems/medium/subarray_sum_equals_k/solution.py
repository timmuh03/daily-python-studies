"""
Docstring for problems.medium.subarray_sum_equals_k.solution
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""



from collections import defaultdict



class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            result += counts[prefix - k]
            counts[prefix] += 1

        return result