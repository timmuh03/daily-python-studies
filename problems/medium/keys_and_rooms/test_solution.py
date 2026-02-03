import pytest
from problems.medium.keys_and_rooms.solution import Solution



@pytest.mark.parametrize("rooms, expected", [
    ([[1],[2],[3],[]], True),

    ([[1,3],[3,0,1],[2],[0]], False),

    ([[2], [], [1]], True),

    ([[],[]], False),

    ([[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]], True)
])


def test_canVisitAllRooms(rooms, expected):
    result = Solution().canVisitAllRooms(rooms)
    assert result == expected, f"Failed on rooms:{rooms}, expected:{expected}"