"""
Docstring for problems.medium.minimum_number_of_arrows_to_burst_balloons.solution

There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] 
denotes a balloon whose horizontal diameter stretches between xstart and xend. 
You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, 
bursting any balloons in its path.
Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Constraints:
1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
"""



class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points: return 0

        # Sort by left boundary so only the right boundary must be tracked.
        balloons = sorted(points, key=lambda x: x[0]) 

        arrow_count = 1
        _, overlap_r = balloons[0] # Rightmost position where an arrow can pop the active group.
        
        for i in range(1, len(balloons)):
            balloon_l, balloon_r = balloons[i]
            if overlap_r < balloon_l: # No overlap; need another arrow.
                arrow_count += 1
                _, overlap_r = balloons[i]
            else:
                overlap_r = min(overlap_r, balloon_r)

        return arrow_count