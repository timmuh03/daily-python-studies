import pytest
from problems.medium.swap_nodes_in_pairs.solution import Solution
from src.utils.list_single import build_list, to_list



@pytest.mark.parametrize("head, expected", [
    ([1, 2, 3, 4], [2, 1, 4, 3]),

    ([], []),

    ([1, 2, 3], [2, 1, 3])
])

def test_swapPairs(head, expected):
    l_head = build_list(head)

    result_head = Solution().swapPairs(l_head)
    assert to_list(result_head) == expected, f"Failed on NodeList:{head}, expected:{expected}, result:{to_list(result_head)}"