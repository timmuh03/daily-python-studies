import pytest
from problems.medium.word_search.solution import Solution



@pytest.mark.parametrize("board, word, expected", [
    ([["A", "B", "C", "E"],
      ["S", "F", "C", "S"],
      ["A", "D", "E", "E"]],
      "ABCCED", True),

    ([["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]], 
      "SEE", True),

    ([["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]],
      "ABCB", False),
])


def test_exist(board, word, expected):
    result = Solution().exist(board, word)
    board_out = '\n'.join(" ".join(row) for row in board)
    assert result == expected, f"Failed on board:\n{board_out}\n, word:{word}, expected:{expected}, result:{result}"