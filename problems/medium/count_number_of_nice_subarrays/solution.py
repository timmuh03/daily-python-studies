"""
Docstring for problems.medium.count_number_of_nice_subarrays.solution
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""



from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
        Returns the count of contiguous subarrays which contain exactly k odd numbers.
        """
        # odd_sum for measuring running sum of odds
        # result for counting 'nice' subarrays
        odd_sum = result = 0
        # counts maps each value of odd_sum to how many times it has occured
        counts = defaultdict(int)
        # seed for a virtual starting position
        counts[0] = 1

        for num in nums:
            if num % 2 == 1:
                odd_sum += 1
                
            if odd_sum - k in counts:
                result += counts[odd_sum - k]

            counts[odd_sum] += 1
            
        return result