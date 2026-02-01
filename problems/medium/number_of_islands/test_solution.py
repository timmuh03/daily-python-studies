import pytest
from problems.medium.number_of_islands.solution import Solution



@pytest.mark.parametrize("grid, expected", [
    ([["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]],
      1),
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]],
      3)
])


def test_numIslands(grid, expected):
    result = Solution().numIslands(grid)
    grd_str = "\n".join(" ".join(map(str, row)) for row in grid)
    assert result == expected, f"Failed on\n{grd_str}\nexpected:{expected}, result:{result}"