"""
Docstring for problems.medium.max_area_of_island.solution

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid 
are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""



class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def explore_island(seed):
            # explore the island
            land = [seed]
            explored.add(seed)
            area = 1
            dirs = [(-1,0), (1,0), (0,-1), (0,1)]
            rows = len(grid)
            cols = len(grid[0])

            while land:
                x, y = land.pop()

                for dir in dirs:
                    dx, dy = dir
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in explored:
                        if grid[nx][ny] == 1:
                            explored.add((nx, ny)) # Prevent counting duplicate land pieces.
                            land.append((nx, ny))
                            area += 1
                
            return area
        
        explored = set()
        max_size = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r, c) not in explored:
                    seed = (r,c)
                    island_size = explore_island(seed)
                    max_size = max(island_size, max_size)

        return max_size
        