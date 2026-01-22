"""
Docstring for problems.medium.kth_largest_element_in_an_array.solution

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return -1