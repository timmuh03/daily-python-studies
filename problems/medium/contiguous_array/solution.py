"""
Docstring for problems.medium.contiguous_array.solution
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
"""



class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        return -1