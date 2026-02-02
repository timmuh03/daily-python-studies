import pytest
from problems.easy.flood_fill.solution import Solution


@pytest.mark.parametrize("image, sr, sc, color, expected", [
    ([[1,1,1],
      [1,1,0],
      [1,0,1]], 1, 1, 2,
      [[2,2,2],
       [2,2,0],
       [2,0,1]]),

    ([[0,0,0],
      [0,0,0]], 0, 0, 0,
      [[0,0,0],
       [0,0,0]])
])


def test_floodFill(image, sr, sc, color, expected):
    result = Solution().floodFill(image, sr, sc, color)
    assert result == expected, f"Failed on image:{image}, expected:{expected}, result:{result}"