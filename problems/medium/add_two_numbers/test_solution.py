import pytest
from problems.medium.add_two_numbers.solution import Solution
from src.utils.list_single import build_list, to_list



@pytest.mark.parametrize("l1, l2, expected", [
    ([2,4,3], [5,6,4], [7,0,8]),

    ([0], [0], [0]),

    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
])

def test_addTwoNumbers(l1, l2, expected):
    l1_head = build_list(l1)
    l2_head = build_list(l2)

    out_head = Solution().addTwoNumbers(l1_head, l2_head)
    assert to_list(out_head) == expected, f"Failed on l1:{l1}, l2:{l2}, expected:{expected}, result:{out_head}"