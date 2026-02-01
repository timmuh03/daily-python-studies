"""
Docstring for problems.medium.number_of_islands.test_solution

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""



class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def count_island(seed):

            land = [seed]
            explored.add(seed)
            dirs = [(-1,0), (1,0), (0,-1), (0,1)]
            rows = len(grid)
            cols = len(grid[0])

            while land:
                x, y = land.pop()

                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in explored:
                        if grid[nx][ny] == "1":
                            explored.add((nx, ny)) # Prevent counting duplicate land pieces.
                            land.append((nx, ny))

        explored = set()
        island_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r,c) not in explored:
                    count_island((r,c)) # Adds all land coords to explored to avoid recounting an island
                    island_count += 1

        return island_count
