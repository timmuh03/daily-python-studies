"""
Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

 
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""



class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1: # Only able to have two sums equal if total is even.
            return False
        can = [False] * (total_sum // 2 + 1)
        target = len(can) - 1
        can[0] = True
        

        for num in nums:
            if num > target: # Won't be able to have two subsets of equal sum
                return False
            for i in range(target - num, -1, -1): # Loop backwards to avoid multiple additions
                if can[i] == True:
                    can[i + num] = True
            
        return can[target]