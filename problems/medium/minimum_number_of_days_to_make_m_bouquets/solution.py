"""
Docstring for problems.medium.minimum_number_of_days_to_make_m_bouquets.solution

You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] 
and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. 
If it is impossible to make m bouquets return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed 
and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Constraints:
bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n
"""




class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1 # Impossible to make correct number of bouquets.
        def check_valid(guess):
            flower_count = 0 # Count of flowers for the bouquet
            bouquet_count = 0 # Count of bouquets
            for flower in bloomDay:
                if flower <= guess: # Flower has bloomed and can be used in a bouquet
                    flower_count += 1
                    if flower_count == k: # Completed a bouquet; reset flowers to not reuse
                        bouquet_count += 1
                        flower_count = 0
                else:
                    flower_count = 0

            return bouquet_count >= m # If true, enough bouquets can be made
        
        high = max(bloomDay)
        low = min(bloomDay)

        while low < high:
            mid = (low + high) // 2
            if check_valid(mid): # feasible; try earlier days
                high = mid
            else: # infeasable; try later days
                low = mid + 1
        return low