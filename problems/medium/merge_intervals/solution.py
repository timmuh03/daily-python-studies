"""
Docstring for problems.medium.merge_intervals.solution

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""



class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sorted_intervals = sorted(intervals)
        lt_bound = sorted_intervals[0][0]
        rt_bound = sorted_intervals[0][1]
        solution = []

        for l, r in sorted_intervals[1:]:
            if l <= rt_bound:
                rt_bound = max(r, rt_bound)
            else:
                solution.append([lt_bound, rt_bound])
                lt_bound = l
                rt_bound = r

        solution.append([lt_bound, rt_bound])

        return solution