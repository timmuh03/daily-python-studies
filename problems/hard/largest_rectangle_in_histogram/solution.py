"""
Docstring for problems.hard.largest_rectangle_in_histogram.solution
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle has an area = 10 units.

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""



class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        my_heights = heights[:]
        my_heights.append(0)
        valid = []
        max_rect = 0

        for i in range(len(my_heights)):
            start = i

            while valid and my_heights[i] < valid[-1][0]:
                height, start = valid.pop()
                curr_rect = (i - start) * height
                if curr_rect > max_rect:
                    max_rect = curr_rect
            if not valid or my_heights[i] > valid[-1][0]:
                valid.append((my_heights[i], start))

        return max_rect