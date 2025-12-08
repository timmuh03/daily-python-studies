import pytest
from .solution import Solution


@pytest.mark.parametrize("matrix, expected", [
    # Larger matrix
    ([  [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 2, 0],
        [0, 0, 0, 0]], [2, 3]),
    
    # Horizontal movement
    ([  [0,0,0],
        [1,2,0],
        [0,0,0]], [1, 2]),

    # Vertical movement
    ([  [0,0,0],
        [0,2,0],
        [0,1,0]], [0, 1]),

    # Diagonal movement
    ([  [1,0,0],
        [0,2,0],
        [0,0,0]], [2, 2]),

    # Bounce off top wall
    ([  [0,0,2],
        [0,0,1],
        [0,0,0]], [1, 2]),

    # Bounce off top wall diagonally
    ([  [0,2,0],
        [1,0,0],
        [0,0,0]], [1, 2]),

    # Bounce off corner
    ([  [0,0,2],
        [0,1,0],
        [0,0,0]], [1, 1]),
])

def test_next_position(matrix, expected: tuple):
    sol = Solution()
    result = sol.get_next_location(matrix)
    assert result == expected, f"Failed for matrix:'{matrix}"
