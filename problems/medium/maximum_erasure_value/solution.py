"""
Docstring for problems.medium.maximum_erasure_value.solution

You are given an array of positive integers nums and want to erase a subarray containing unique elements. 
The score you get by erasing the subarray is equal to the sum of its elements.
Return the maximum score you can get by erasing exactly one subarray.
An array b is called to be a subarray of a if it forms a contiguous subsequence of a, 
that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""



class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = 0
        cur_sum = 0 
        max_sum = 0
        subarray = set() # need O(1) access for a unique subarray

        for num in nums:
            if num in subarray: # Adding num to subarray if already present would make it invalid
                while num in subarray:
                    x = nums[left]
                    subarray.remove(x)
                    cur_sum -= x
                    left += 1
            subarray.add(num)
            cur_sum += num
            if cur_sum > max_sum: max_sum = cur_sum

        return max_sum