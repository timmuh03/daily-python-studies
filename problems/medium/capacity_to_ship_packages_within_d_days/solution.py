"""
Docstring for capacity_to_ship_packages_withing_d_days.solution
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt 
(in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Constraints:
1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500
"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        hi = sum(weights)
        lo = max(weights)
        while lo != hi:
            day = 1
            guess = (hi + lo) // 2
            packed = 0
            for weight in weights:
                if packed + weight > guess:
                    day += 1
                    packed = weight
                    if day > days:
                        break
                    continue
                packed += weight
            if day > days:
                lo = guess + 1
            else:
                hi = guess
        return lo