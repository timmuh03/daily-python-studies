import pytest

from problems.medium.maximum_width_of_binary_tree.solution import Solution
from src.utils.tree import build_tree



@pytest.mark.parametrize("tree_list, expected", [
    ([1,3,2,5,3,None,9], 4),
    ([1,3,2,5,None,None,9,6,None,7], 7),
    ([1,3,2,5], 2),
    ([1,1,1,1,1,1,1,None,None,None,1,None,None,None,None,2,2,2,2,2,2,2,None,2,None,None,2,None,2], 8),
    ([1,None,2], 1)
])


def test_widthOfBinaryTree(tree_list, expected):
    root = build_tree(tree_list)
    result = Solution().widthOfBinaryTree(root)
    assert result == expected, f"Failed on root:{tree_list}, expected:{expected}, result:{result}"