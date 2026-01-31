import pytest
from problems.medium.max_area_of_island.solution import Solution



@pytest.mark.parametrize("grid, expected", [
    (
        [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]],
         6
    ),
    (
        [[0,0,0,0,0,0,0,0]],
        0
    )
])


def test_maxAreaOfIsland(grid, expected):
    result = Solution().maxAreaOfIsland(grid)
    grid_str = "\n".join(" ".join(map(str, row)) for row in grid)
    assert result == expected, f"Failed on grid:\n{grid_str}\nexpected:{expected}, result:{result}"