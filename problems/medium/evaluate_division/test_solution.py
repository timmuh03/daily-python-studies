import pytest
from problems.medium.evaluate_division.solution import Solution



@pytest.mark.parametrize("equations, values, queries, expected", [
    ([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],  
     [6.00000,0.50000,-1.00000,1.00000,-1.00000]),

    ([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]],
     [3.75000,0.40000,5.00000,0.20000]),

    ([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]],
     [0.50000,2.00000,-1.00000,-1.00000]),

    ([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]],
     [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000])
])


def test_calcEquation(equations, values, queries, expected):
    result = Solution().calcEquation(equations, values, queries)
    assert result == pytest.approx(expected, abs=1e-5), f"Failed on equatoins:{equations}, values:{values}, queries:{queries}, expected:{expected}, result:{result}"