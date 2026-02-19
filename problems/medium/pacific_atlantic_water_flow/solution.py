"""
Docstring for problems.medium.pacific_atlantic_water_flow.solution

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights 
where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


Example 1:

Input: heights =    [[1,2,2,3,5],
                    [3,2,3,4,4],
                    [2,4,5,3,1],
                    [6,7,1,4,5],
                    [5,1,1,2,4]]

Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
"""



class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        def flood(starts: set[tuple]) -> set[tuple]:
            visited = set(starts)
            stack = list(starts)

            while stack:
                curr = stack.pop()
                ortho_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dir in ortho_dirs:
                    x = dir[0] + curr[0]
                    y = dir[1] + curr[1]

                    if 0 <= x < len(heights) and 0 <= y < len(heights[0]):
                        if (x,y) not in visited:
                            if heights[curr[0]][curr[1]] <= heights[x][y]:
                                stack.append((x, y))
                                visited.add((x,y))

            return visited
                        




        # Grab just the outside coords of heights.
        pacific_starts = set()
        atlantic_starts = set()
        rows = len(heights)
        cols = len(heights[0])
        for j in range(cols):
            # Top row
            pacific_starts.add((0, j))
            # Bottom row
            atlantic_starts.add((rows - 1, j))

        for i in range(rows):
            # Left column
            pacific_starts.add((i, 0))
            #right column
            atlantic_starts.add((i, cols - 1,))

        pacific_peaks = flood(pacific_starts)
        atlantic_peaks = flood(atlantic_starts)

        result = []

        for coord in pacific_peaks:
            if coord in atlantic_peaks:
                result.append(list(coord))

        return result




        