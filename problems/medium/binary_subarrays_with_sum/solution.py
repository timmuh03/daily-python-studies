"""
Docstring for problems.medium.binary_subarrays_with_sum.solution
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are in single quotes below:
['1,0,1',0,1]
['1,0,1,0',1]
[1,'0,1,0,1']
[1,0,'1,0,1']
"""



class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        return -1