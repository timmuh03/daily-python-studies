import pytest
from problems.hard.find_median_from_data_stream.solution import MedianFinder



def _reference_median(nums: list[int]) -> float:
    s = sorted(nums)
    n = len(s)
    if n % 2 == 1:
        return float(s[n // 2])
    return (s[n // 2 - 1] + s[n // 2]) / 2


def _run_ops(ops: list[tuple[str, int | None]]) -> list[float]:

    mf = MedianFinder()
    seen: list[int] = []
    out: list[float] = []

    for op, arg, in ops:
        if op == 'add':
            assert arg is not None
            mf.addNum(arg)
            seen.append(arg)
        elif op == 'median':
            got = mf.findMedian()
            exp = _reference_median(seen)
            out.append(got)
            assert got == exp

            got2 = mf.findMedian()
            assert got2 == got
        else:
            raise ValueError(f"Unknown op: {op}")
        
    return out


def test_leetcode_style_squence() -> None:

    ops = [
        ('add', -1),
        ('median', None),
        ('add', -1),
        ('median', None),
        ('add', 2),
        ('median', None),
        ('add', 2),
        ('median', None),
        ('add', 2),
        ('median', None),
    ]
    _run_ops(ops)


def test_mixed_inserts_more_queries() -> None:
    ops = [
        ("add", 10),
        ("add", 1),
        ("add", 9),
        ("median", None),
        ("add", 2),
        ("median", None),
        ("add", 8),
        ("add", 3),
        ("median", None),
        ("add", 7),
        ("add", 4),
        ("add", 6),
        ("median", None),
        ("add", 5),
        ("median", None),
    ]
    _run_ops(ops)


def test_range_extremes() -> None:
    ops = [
        ("add", -100000),
        ("median", None),
        ("add", 100000),
        ("median", None),
        ("add", 0),
        ("median", None),
    ]
    _run_ops(ops)

def test_extra() -> None:
    ops = [
        ('add', -1),
        ('median', None),
        ('add', -2),
        ('median', None),
        ('add', -3),
        ('median', None),
        ('add', -4),
        ('median', None),
        ('add', -5),
        ('median', None),
    ]
    _run_ops(ops)