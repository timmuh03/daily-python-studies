import pytest
from utils.tree import build_tree
from binary_tree_right_side_view.solution import Solution



@pytest.mark.parametrize("input_list, expected", [
    ([1,2,3,None,5,None,4], [1,3,4]),
    ([1,2,3,4,None,None,None,5], [1,3,4,5]),
    ([1,None,3], [1,3]),
    ([], [])
])


def test_rightSideView(input_list, expected):
    root = build_tree(input_list)
    result = Solution().rightSideView(root)
    assert result == expected, f"Failed on root:{input_list}, expected:{expected}, result:{result}"
   