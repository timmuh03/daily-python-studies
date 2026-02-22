import pytest
from problems.medium.snapshot_array.solution import SnapshotArray



@pytest.fixture()
def snapshot_array(length: int):
    return SnapshotArray(length)


@pytest.mark.parametrize("ops", [
    [
        ("init", 3),
        ("set", 0, 5),
        ("snap", 0),
        ("set", 0, 6),
        ("get", 0, 0, 5),
    ],

    [
        ("init", 2),
        ("set", 0, 7),
        ("set", 1, 9),
        ("snap", 0),
        ("set", 0, 1),
        ("get", 0, 0, 7),
        ("get", 1, 0, 9),
    ],

    [
        ("init", 1),
        ("set", 0, 4),
        ("snap", 0),
        ("snap", 1),
        ("snap", 2),
        ("get", 0, 2, 4),
        ("get", 0, 1, 4),
        ("get", 0, 0, 4),
    ],

    [
        ("init", 1),
        ("set", 0, 1),
        ("set", 0, 2),
        ("set", 0, 3),
        ("snap", 0),
        ("get", 0, 0, 3),
    ],
])

def test_snapshot_array_scripts(ops):
    arr = None
    for op in ops:
        op_name = op[0]

        if op_name == "init":
            _, length = op
            arr = SnapshotArray(length)

        elif op_name == "set":
            assert arr is not None, "SnapshotArray must be initialized before set"
            _, index, val = op
            arr.set(index, val)

        elif op_name == "snap":
            assert arr is not None, "SnapshotArray must be initialized before snap"
            _, expected_snap_id = op
            got = arr.snap()
            assert got == expected_snap_id

        elif op_name == "get":
            assert arr is not None, "SnapshotArray must be initialized before get"
            _, index, snap_id, expected_val = op
            got = arr.get(index, snap_id)
            assert got == expected_val

        else:
            pytest.fail(f"Unknown op: {op}")