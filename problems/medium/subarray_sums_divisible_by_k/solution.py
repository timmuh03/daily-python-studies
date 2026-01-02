"""
Docstring for problems.medium.subarray_sums_divisible_by_k.solution
Given an integer array nums and an integer k, return the number of non-empty subarrays 
that have a sum divisible by k.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Constraints:
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
"""



from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        rem = 0
        counts = defaultdict(int) # number of prefixes seen so far with remainder k
        counts[0] = 1
        result = 0

        for num in nums:
            rem = (rem + num) % k
            result += counts[rem]
            counts[rem] += 1


        return result