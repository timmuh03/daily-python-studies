"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""



class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums_set:
            if num - 1 not in nums_set: # Only start at sequence starts
                curr_count = 1

                while num + 1 in nums_set:
                    num += 1 # Walking num doesn't affect iteration over nums_set
                    curr_count += 1

                if curr_count > max_count: max_count = curr_count

        return max_count
