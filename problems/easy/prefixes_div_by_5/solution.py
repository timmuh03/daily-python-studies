"""
Docstring for problems.prefixes_div_by_5.solution
You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] 
(from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
"""

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result = []
        remainder = 0
        for bit in nums:
            # remainder = (remainder << 1 | bit) bitwise operation to so the same as below
            remainder = (remainder * 2  + bit) % 5 # only need remainder to figure divisibility
            result.append(remainder == 0)
                
        return result