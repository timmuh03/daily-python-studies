"""
Docstring for problems.hard.split_array_largest_sum.solution

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)
"""



class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # Check if nums can be split into <= k subarrays with the max sum being <= limit
        def check_valid(limit):
            subarray_count = 1
            current_sum = 0
            for num in nums:
                if num > limit: return False
                if num + current_sum > limit: # Enforce subarray max sum by starting a new subarray
                    subarray_count += 1
                    current_sum = 0
                if subarray_count > k: return False # Early exit when exceeded allowed subarrays
                current_sum += num

            return True
        
        low = max(nums)
        high = sum(nums)

        while low < high: # Convergance loop
            mid = (low + high) // 2

            valid = check_valid(limit=mid)
            if valid: high = mid
            else: low = mid + 1
        return low