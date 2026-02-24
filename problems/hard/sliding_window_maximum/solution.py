"""
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


 Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        def push_index(i):
            # Maintain candidates in decreasing value so candidates[0] is window max.
            # Anything smaller than nums[i] can never be max again.
            while candidates and nums[candidates[-1]] < nums[i]:
                candidates.pop()

            candidates.append(i)

        L = 0
        candidates = deque()
        result = []

        # Build first window to save frequent R >= k checks later
        for R in range(k):
            push_index(R)

        curr_max = nums[candidates[0]]
        result.append(curr_max)

        for R in range(k, len(nums)):
            L += 1
            while candidates and candidates[0] < L: 
                candidates.popleft() # candidates[0] left the window
            push_index(R)
            result.append(nums[candidates[0]])

        return result


