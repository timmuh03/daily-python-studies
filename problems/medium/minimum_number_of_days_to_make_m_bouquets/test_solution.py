import pytest
from problems.medium.minimum_number_of_days_to_make_m_bouquets.solution import Solution



@pytest.mark.parametrize("bloomDay, m, k, expected", [
    ([1,10,3,10,2], 3, 1, 3),
    ([1,10,3,10,2], 3, 2, -1),
    ([7,7,7,7,12,7,7], 2, 3, 12)
])


def test_minDays(bloomDay, m, k, expected):
    result = Solution().minDays(bloomDay, m, k)
    assert result == expected, f"Failed on bloomDay={bloomDay}, m={m}, k={k}, expected={expected}, result={result}"
    