import pytest
from problems.medium.asteriod_collision.solution import Solution



@pytest.mark.parametrize("asteroids, expected", [
    ([5, 10, -5], [5, 10]),

    ([8, -8], []),

    ([10, 2, -5], [10]),

    ([3, 5, -6, 2, -1, 4], [-6, 2, 4]),

    ([-2, 1, 1, -1], [-2, 1]),

    ([1,-1,-2,-2], [-2, -2]),

    ([-2, -1], [-2, -1])
])



def test_asteroidCollision(asteroids, expected):
    result = Solution().asteroidCollision(asteroids)
    assert result == expected, f"Failed on asteroids:{asteroids}, expected:{expected}, result:{result}"