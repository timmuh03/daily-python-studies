"""
Docstring for problems.medium.subarray_product_less_than_k.solution

Given an array of integers nums and an integer k, return the number of contiguous subarrays 
where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Constraints:
1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""



class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0 # Product can never be < 1
        
        left = 0 # left boundary/pointer
        product = 1 # first number must be calculated as itself
        result = 0

        for i, num in enumerate(nums):
            product = product * num # calculate product for window ending at new right boundary

            while product >= k: # restore validity with smallest valid index
                product = product // nums[left] # floor div to keep ints
                left += 1 # move left boundary up one

            result += i - left + 1 # all subarrays left -> i are considered valid

        return result