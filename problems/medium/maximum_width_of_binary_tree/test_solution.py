import pytest

from problems.medium.maximum_width_of_binary_tree.solution import Solution
from src.utils.tree import build_tree



@pytest.mark.parametrize("tree_list, expected", [
    ([1,3,2,5,3,None,9], 4),
    ([1,3,2,5,None,None,9,6,None,7], 7),
    ([1,3,2,5], 2)
])


def test_widthOfBinaryTree(tree_list, expected):
    root = build_tree(tree_list)
    result = Solution().widthOfBinaryTree(root)
    assert result == expected, f"Failed on root:{tree_list}, expected:{expected}, result:{result}"