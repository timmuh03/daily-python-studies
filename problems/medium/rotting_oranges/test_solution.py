import pytest
from problems.medium.rotting_oranges.solution import Solution



@pytest.mark.parametrize("grid, expected", [
    ([[2,1,1,],
      [1,1,0],
      [0,1,1]], 4),

    ([[2,1,1],
      [0,1,1],
      [1,0,1]], -1),

    ([[0,2]], 0),

    ([[2,1,1],
      [1,1,1],
      [0,1,2]], 2),

    ([[2,1]], 1),

    ([[2]], 0),

    ([[1]], -1),

    ([[2,1,1]], 2),

    ([[2,0,1]], -1)
])


def test_orangesRotting(grid, expected):
    grid_out = "\n".join(str(a) for a in grid)
    result = Solution().orangesRotting(grid)
    assert result == expected, f"\nFailed on grid:\n{grid_out}\nexpected: {expected}, result: {result}"