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


import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        group = nums[:k]
        heapq.heapify(group)
        for num in nums[k:]:
            if num > group[0]:
                heapq.heappushpop(group, num)
        return group[0]

        ### This does pretty much the same thing without being as explicit
        # group = nums
        # result = heapq.nlargest(k, group)
        # return min(result)