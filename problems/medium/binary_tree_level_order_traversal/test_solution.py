import pytest
from src.utils.tree import build_tree
from problems.medium.binary_tree_level_order_traversal.solution import Solution



@pytest.mark.parametrize("input_list, expected", [
    ([3, 9, 20, None, None, 15, 7], 
     [[3], [9, 20], [15, 7]]),

     ([1], [[1]]),

     ([], [])
])


def test_levelOrder(input_list, expected):
    root = build_tree(input_list)
    result = Solution().levelOrder(root)
    assert result == expected, f"Failed on root:{input_list}, expected:{expected}, result:{result}"