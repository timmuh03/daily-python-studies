import pytest
from problems.medium.redundant_connection.solution import Solution



@pytest.mark.parametrize("edges, expected", [
    ([[1,2], [1,3], [2,3]], [2,3]),

    ([[1,2], [2,3], [3,4], [1,4], [1,5]], [1,4]),

    ([[3,7],[1,4],[2,8],[1,6],[7,9],[6,10],[1,7],[2,3],[8,9],[5,9]], [8,9]),

    ([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]], [4,10])
])


def test_findRedundantConnection(edges, expected):
    result = Solution().findRedundantConnection(edges)
    assert result == expected, f"Failed on edges:{edges}, expected:{expected}, result:{result}"