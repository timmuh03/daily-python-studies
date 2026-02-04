import pytest
from problems.medium.non_overlapping_intervals.solution import Solution



@pytest.mark.parametrize("intervals, expected", [
    ([[1,2],[2,3],[3,4],[1,3]], 1),
    ([[1,2],[1,2],[1,2]], 2),
    ([[1,2],[2,3]], 0),
    ([[0,2],[1,3],[2,4],[3,5],[4,6]], 2)
])


def test_eraseOverlapIntervals(intervals, expected):
    result = Solution().eraseOverlapIntervals(intervals)
    assert result == expected, f"Failed on intervals:{intervals}, expected:{expected}, result:{result}"