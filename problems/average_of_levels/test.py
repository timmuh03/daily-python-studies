import pytest
from .solution import Solution
from utils import build_tree



@pytest.mark.parametrize("input_list, expected",[
    ([3,9,20,None,None,15,7],
     [3.0, 14.5, 11.0]),
    
    ([3, 9, 20, 15, 7], 
     [3.0, 14.5, 11.0]),   
    
    ([1], 
     [1.0]),   
    
    ([], []),
    (None, []),
    
    ([1, 2, 3, 4, 5], 
     [1.0, 2.5, 4.5]),    
    
    ([2147483647, 2147483647, 2147483647], 
     [2147483647.0, 2147483647.0]),  
    
    ([1, None, 2, None, 3], 
     [1.0, 2.0, 3.0]),    
    
    ([5, 8, 9, 2, 1, 3, 7, 4, 6], 
     [5.0, 8.5, 3.25, 5.0]),
])

def test_average_of_levels(input_list, expected):
    sol = Solution()
    root = build_tree(input_list)
    result = sol.averageOfLevels(root) 
    assert len(result) == len(expected), f"Failed on input_list:{input_list} expected:{expected} result:{result}"
    for a, b in zip(result, expected):
        assert abs(a - b) < 1e-5
    