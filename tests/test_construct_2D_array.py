import pytest
from construct_2D_array.solution import Solution

@pytest.mark.parametrize("original, m, n, expected", [
    # Basic test
    ([1,2,3,4], 2, 2, 
     [[1,2], [3,4]]),
    
    # Return one list
    ([1,2,3], 1, 3,
     [[1,2,3]]),
    
    #Big numbers
    ([10000, 20000, 30000, 40000], 2, 2,
     [[10000, 20000],[30000, 40000]]),
    
    # Tall one element per list
    ([1, 2, 3, 4], 4, 1,
     [[1], [2], [3], [4]]),
    
    # Length doesn't fit dimensions
    ([1,2,3], 2, 2,
     []),
    
    # Empty inputs
    ([], 0, 0,
     []),
    
    ([], 1, 1,
     []),
    
    # Single element
    ([42], 1, 1,
     [[42]]),
    
    # Rectangular 2x3
    ([1,2,3,4,5,6], 2, 3,
     [[1,2,3], [4,5,6]]),
    
    # Rectangle 3x2
    ([1,2,3,4,5,6], 3, 2,
     [[1,2], [3,4], [5,6]]),
    
    # Larger rectangle
    (list(range(1, 21)), 4, 5,
     [
         [1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20]
     ]),
    
    # Negative numbers
    ([0, -1, 7, 1000], 2, 2,
     [[0, -1,], [7, 1000]]),
    
    # Duplicate values
    ([5, 5, 5, 5], 2, 2,
     [[5, 5], [5, 5]])
       
])

def test_construct_2D_array(original: list[int], m: int, n: int, expected:list[list[int]]):
    sol = Solution()
    result = sol.construct2DArray(original, m, n)
    assert result == expected, f"Failed for og: {original}, m:{m}, n:{n},  -  result:{result} expected:{expected}"