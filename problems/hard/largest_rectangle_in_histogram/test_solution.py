import pytest
from largest_rectangle_in_histogram.solution import Solution



@pytest.mark.parametrize("heights, expected", [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4)
])



def test_largestRectangleArea(heights, expected):
    result = Solution().largestRectangleArea(heights)
    assert result == expected, f"Failed on heights:{heights}, expected:{expected}, result:{result}"