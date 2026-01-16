import pytest
from problems.medium.binary_tree_level_order_traversal.solution import Solution



@pytest.mark.parametrize("input_list, expected", [
    ([3, 9, 20, None, None, 15, 7], 
     [[3], [9, 20], [15, 7]]),

     ([1], [[1]]),

     ([], [])
])


def test_levelOrder(input_list, expected):
    result = Solution().levelOrder(input_list)
    assert result == expected, f"Failed on root:{input_list}, expected:{expected}, result:{result}"