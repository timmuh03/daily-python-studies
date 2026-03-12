import pytest
from src.utils.tree import tree_to_level_list
from problems.medium.construct_binary_tree_from_preorder_and_inorder_traversal.solution import Solution



@pytest.mark.parametrize("preorder, inorder, expected", [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7],
     [3, 9, 20, None, None, 15, 7]),

    ([-1], [-1],
     [-1])
])

def test_buildTree(preorder, inorder, expected):
    root = Solution().buildTree(preorder, inorder)
    result = tree_to_level_list(root)
    assert result == expected, (
        f"Failed on preorder:{preorder}, inorder:{inorder}, expected:{expected}, result:{result}"
    )