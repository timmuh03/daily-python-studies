import pytest
from problems.medium.online_stock_span.solution import StockSpanner



@pytest.mark.parametrize("prices, expected", [
    ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
    ([10, 20, 30, 40], [1, 2, 3, 4]),
    ([40, 30, 20 ,10], [1, 1, 1, 1]),
    ([80, 80, 80], [1, 2, 3]),
    ([31, 41, 48, 59, 79], [1, 2, 3, 4, 5])
])


def test_stockSpanner(prices, expected):
    spanner = StockSpanner()
    result = [spanner.next(p) for p in prices]
    assert result == expected, f"Failed on prices:{prices}, expected:{expected}, result:{result}"