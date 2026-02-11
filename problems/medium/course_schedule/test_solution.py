import pytest
from problems.medium.course_schedule.solution import Solution



@pytest.mark.parametrize("numCourses, prerequisites, expected", [
    (2, [[1,0]], True),

    (2, [[1,0], [0,1]], False),
])


def test_canFinish(numCourses, prerequisites, expected):
    result = Solution().canFinish(numCourses, prerequisites)
    assert result == expected, f"Failed on numCourses:{numCourses}, prerequisites:{prerequisites}, expected:{expected}, result:{result}"
    