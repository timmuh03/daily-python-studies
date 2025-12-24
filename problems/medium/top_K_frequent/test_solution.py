import pytest
from .solution import Solution


@pytest.mark.parametrize("nums, k, expected", [
    ([1,1,1,2,2,3], 2,
     [1,2]),
    
    ([1], 1,
     [1]),
    
    ([1,2,1,2,1,2,3,1,3,2], 2,
     [1, 2]),
    
    ([2,2,3,3,3,1,1,1,1], 2,
     [1, 3])
])


def test_top_K_frequent(nums, k, expected):
    result = Solution().topKFrequent(nums, k)
    assert result == expected, f"Failed on nums:{nums}, k:{k}, expected:{expected}, result{result}"