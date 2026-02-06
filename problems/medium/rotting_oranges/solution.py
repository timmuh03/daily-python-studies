"""
Docstring for problems.medium.rotting_oranges.solution

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid =   [[2,1,1],
                [1,1,0],
                [0,1,1]]
Output: 4

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""




from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minutes = -1
        rotten = deque()
        fresh_count = 0

        for row in range(len(grid)):
            for col, cell in enumerate(grid[row]):
                if  cell == 2:
                    rotten.append((row,col))
                elif cell == 1:
                    fresh_count += 1
        if fresh_count == 0: return 0 # Nothing to rot

        ortho = [(1,0), (-1,0), (0,1), (0,-1)]

        round_size = len(rotten)
        while round_size > 0: # Keep going while there's items to process
            r,c = rotten.popleft()
            for dir in ortho:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < len(grid) and 0 <=nc < len(grid[0]): # Skip out-of-bounds checks
                    if grid[nr][nc] == 1: 
                        rotten.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh_count -= 1
            round_size -= 1
            if round_size == 0:
                minutes += 1
                round_size = len(rotten)

        return minutes if not fresh_count else -1