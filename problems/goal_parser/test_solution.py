import pytest
from .solution import Solution

@pytest.mark.parametrize("command, expected", [
    ('G()(al)',
     'Goal'),
    
    ('', 
     ''),
    
    ('()G(al)()',
     'oGalo')
       
])

def test_goal_parser(command, expected):
    sol = Solution()
    result = sol.interpret(command)
    assert result == expected, f"Failed for command:{command}, ecpected:{expected}, result:{result}"
