"""
Docstring for problems.medium.koko_eating_bananas.solution
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas 
and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead 
and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Constraints:
1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""



import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        hi = max(piles)
        lo = 1

        while hi != lo:
            hours = 0
            guess = (lo + hi) // 2
            for pile in piles:
                hours += math.ceil(pile / guess)
            if hours > h:
                lo = guess + 1
            else:
                hi = guess

        return lo