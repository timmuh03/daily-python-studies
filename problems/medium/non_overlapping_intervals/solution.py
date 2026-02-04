"""
Docstring for problems.medium.non_overlapping_intervals.solution

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""



class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        my_intervals = sorted(intervals)
        boundary = my_intervals[0][1]
        count = 0 # Track number of removed intervals

        for i, j in my_intervals[1:]:
            if boundary > i:
                count += 1
                boundary = min(j, boundary)
            else:
                boundary = j

        return count