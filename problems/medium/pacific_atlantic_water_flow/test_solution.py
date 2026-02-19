import pytest
from problems.medium.pacific_atlantic_water_flow.solution import Solution



@pytest.mark.parametrize("heights, expected", [
    ([[1,2,2,3,5],
      [3,2,3,4,4,],
      [2,4,5,3,1,],
      [6,7,1,4,5,],
      [5,1,1,2,4,]],
      [[0,4], [1,3], [1,4], [2,2], [3,0],  [3,1], [4,0]]),

    ([[1]],
     [[0,0]])
])


def test_pacificAtlantic(heights, expected):
    result = Solution().pacificAtlantic(heights)

    result_set = {tuple(rc) for rc in result}
    expected_set = {tuple(rc) for rc in expected}

    heights_out = '\n'.join(' '.join(str(x) for x in row) for row in heights)
    assert result_set == expected_set, f"Failed on heights:\n{heights_out}\nexpected:{expected}, result:{result}"