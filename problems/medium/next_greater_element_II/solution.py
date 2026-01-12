"""
Docstring for problems.medium.next_greater_element_II.solution
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""



class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        result = [-1] * len(nums)
        unresolved = []

        for i in range(len(nums)):

            while unresolved and nums[i] > nums[unresolved[-1]]:
                result[unresolved.pop()] = nums[i]
                
            unresolved.append(i)



        for i in range(len(nums)):
            while unresolved and nums[i] > nums[unresolved[-1]]:
                result[unresolved[-1]] = nums[i]
                unresolved.pop()
            if not unresolved:
                return result


        return result