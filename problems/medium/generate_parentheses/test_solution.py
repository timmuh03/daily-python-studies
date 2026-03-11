import pytest
from problems.medium.generate_parentheses.solution import Solution



@pytest.mark.parametrize("n, expected", [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),

    (1, ["()"])
])

def test_generateParentheses(n, expected):
    result = Solution().generateParenthesis(n)
    assert result == expected, f"Failed on n:{n}, expected:{expected}, result:{result}"