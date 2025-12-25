import pytest
from .solution import Solution

@pytest.mark.parametrize("brackets, income, expected", [
    ([[3,50], [7,10], [12,25]], 10,
     2.65),
    
    ([[0, 10], [10, 50], [20, 10]], 15,
     5.5),
    
    ([[5, 10], [10, 20], [20, 30]], 10,
     1.5),
    
    ([[5, 10], [10, 20]], 2,
     .2)

])

def test_calculate_tax(brackets, income, expected):
    sol = Solution()
    result = sol.calculateTax(brackets, income)
    assert expected == result, f"Failed for brackets:{brackets}, income:{income}, expected:{expected}, result:{result}"