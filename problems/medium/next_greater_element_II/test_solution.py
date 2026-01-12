import pytest
from next_greater_element_II.solution import Solution



@pytest.mark.parametrize("num, expected", [
    ([1, 2, 1], [2, -1, 2]),
    ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4])
])



def test_nextGreaterElements(num, expected):
    result = Solution().nextGreaterElements(num)
    assert result == expected, f"Failed on num:{num}, expected:{expected}, result:{result}"