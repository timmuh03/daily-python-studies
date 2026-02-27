import pytest
from problems.medium.task_scheduler.solution import Solution



@pytest.mark.parametrize("tasks, n, expected", [
    (["A","A","A","B","B","B"], 2, 8),

    (["A","C","A","B","D","B"], 1, 6),

    (["A","A","A","B","B","B"], 3, 10)
])

def test_leastInterval(tasks, n, expected):
    result = Solution().leastInterval(tasks, n)
    assert result == expected, f"Failed on tasks:{tasks}, n:{n}, expected:{expected}, result:{result}"