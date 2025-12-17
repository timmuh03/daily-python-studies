import pytest
from .solution import Solution

def create_guess(picked):
    def guess(num: int) -> int:
        if num > picked:
            return -1
        elif num < picked:
            return 1
        return 0
    return guess


@pytest.mark.parametrize("n, picked", [
    (10, 1),
    (10, 5),
    (10, 10),
    (100, 73)
])


def test_guess_number(monkeypatch, n, picked):
    from . import solution
    
    monkeypatch.setattr(solution, "guess", create_guess(picked))
    
    result = Solution().guessNumber(n)
    assert result==picked, f"Failed for n:{n} picked:{picked}, result:{result}"
    