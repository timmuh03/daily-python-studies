"""
Docstring for problems.max_containers.solution

You are given a positive integer n representing an n x n cargo deck on a ship. 
Each cell on the deck can hold one container with a weight of exactly w.

However, the total weight of all containers, if loaded onto the deck, 
must not exceed the ship's maximum weight capacity, maxWeight.

Return the maximum number of containers that can be loaded onto the ship. 

Constraints:

1 <= n <= 1000
1 <= w <= 1000
1 <= maxWeight <= 109
"""

class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
            # n*n is max num of containers.
            # if max num of containers' weight is less/equal to maxWeight they can all fit
            # else max num of containters that can fit is determined by maxWeight // container weight (w)
        return n*n if n*n*w <= maxWeight else maxWeight // w