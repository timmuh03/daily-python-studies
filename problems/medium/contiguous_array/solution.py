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
        balance = best = 0
        counts = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                balance -= 1
            elif num == 1:
                balance += 1

            if balance in counts:
                valid = i - counts[balance]
                if valid > best:
                    best = valid
            else:
                counts[balance] = i


        return best