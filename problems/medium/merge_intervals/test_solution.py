import pytest
from problems.medium.merge_intervals.solution import Solution



@pytest.mark.parametrize("intervals, expected", [
    ([[1,3], [2,6], [8,10], [15,18]], [[1,6], [8,10], [15,18]]),

    ([[1,4],[4,5]], [[1,5]]),

    ([[4,7],[1,4]], [[1,7]]),

    ([[1,4],[2,3]], [[1,4]])
])


def test_merge(intervals, expected):
    result = Solution().merge(intervals)
    assert result == expected, f"Failed on intervals:{intervals}, expected:{expected}, result:{result}"