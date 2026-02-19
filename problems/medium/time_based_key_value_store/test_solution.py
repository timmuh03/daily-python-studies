import pytest
from problems.medium.time_based_key_value_store.solution import TimeMap



@pytest.fixture
def time_map():
    return TimeMap()


@pytest.mark.parametrize("ops", [
    [
        ('set', 'foo', 'bar', 1),
        ('get', 'foo', 1, 'bar'),
        ('get', 'foo', 3, 'bar'),
        ('set', 'foo', 'bar2', 4),
        ('get', 'foo', 4, 'bar2'),
        ('get', 'foo', 5, 'bar2'),
    ],
    [
        ('get', 'foo', 1, '')
    ]
])
def test_timemap_scripts(time_map, ops):
    for op in ops:
        if op[0] == 'set':
            op_name, key, value, ts = op
            time_map.set(key, value, ts)
        elif op[0] == 'get':
            op_name, key, ts, expected = op
            result = time_map.get(key, ts)
            assert result == expected

        else: pytest.fail(f"Unknown op: {op[0]}")





