"""
Docstring for problems.medium.minimum_size_subarray_sum.solution

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""



class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = len(nums) + 1
        left = 0
        cur_sum = 0

        for i, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= target:
                temp_len = i + 1 - left
                min_len = min(min_len, temp_len)
                cur_sum -= nums[left]
                
                left += 1

        return min_len if min_len < len(nums) + 1 else 0