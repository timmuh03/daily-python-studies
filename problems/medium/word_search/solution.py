"""
Docstring for word_search.solution

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:

Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]],
             word = "ABCCED"
Output: true


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""


class Solution: 
    def exist(self, board: list[list[str]], word: str) -> bool: 
        def search_next(r: int, c: int, visited: set, i: int):
            i += 1 

            ortho_coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for x, y in ortho_coords:
                x = x + r
                y = y + c
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    if (x, y) not in visited:
                        if board[x][y] == word[i]:
                            if i == len(word) - 1: return True
                            visited.add((x, y))
                            match = search_next(x, y, visited, i)
                            if match: return True
                            visited.remove((x,y))
            return False


        for r, row in enumerate(board): 
            for c, char in enumerate(row): 
                if char == word[0]: 
                    if len(word) == 1: return True
                    coord = (r, c) 
                    visited = {coord}
                    match = search_next(r, c, visited, 0) 
                    if match: return True 
        return False